from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission
from book.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.initial_setup(self, *args, **options)

    def initial_setup(self, *args, **kwars):
        try:
            self.setup_default_user()

        except Exception as e:
            print("default user setup failed", e)
        try:
            client_id, secret = self.setup_application()
            print("Client Id ", client_id)
            print("Client Secret ", secret)
        except Exception as e:
            print("application setup failed", e)

    def setup_default_user(self, *args, **kwars):
        if not User.objects.filter(email="admin@addressbook.com").exists():
            data = {
                "user_type": "su",
                "email": "admin@addressbook.com",
                "is_staff": True,
                "is_active": True,
                "is_superuser": True,
            }
            admin = User.objects.create(**data)
            admin.set_password("swordfish")
            admin.save()

    def setup_application(self, *args, **kwars):
        print("inside this")
        from oauth2_provider.models import Application

        if not Application.objects.all().exists():
            admin = User.objects.get(email="admin@addressbook.com", user_type="su")
            application = Application()
            application.name = "address_book"
            application.user_id = admin.id
            application.client_type = "public"
            application.authorization_grant_type = "password"
            application.redirect_uris = ""

            application.save()

        else:
            application = Application.objects.all().first()
        return application.client_id, application.client_secret
