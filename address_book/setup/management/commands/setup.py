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

        if not User.objects.filter(email="rajesh@book.com").exists():
            data = {
                "user_type": "normal",
                "email": "rajesh@book.com",
                "is_staff": True,
                "is_active": True,
                "is_superuser": False,
            }

            normal_user = User.objects.create(**data)
            normal_user.set_password("swordfish")
            normal_user.save()

    def setup_application(self, *args, **kwars):

        from oauth2_provider.models import Application

        print(Application.objects.all())
        if not Application.objects.all().exists():
            print("inside if")
            admin = User.objects.get(email="admin@addressbook.com", user_type="su")
            data = {
                "name": "Backend",
                "user_id": admin.id,
                "client_id": "wJGKOklUDyeizuz05UANSfYgRFQlHMoYvNJnBhBN",
                "client_secret": "fwfkBrEppx21cdyHwgVsOLenVJobdEtSBWEudrM5y1146ysRCUC0B2KKTIwUY5YDniG3PhlXWCSBudjBafDQynpwr74W1LABJ7GRihy8yjDDj3oxpYIjhrblu8JJjf1U",
                "client_type": "confidential",
                "authorization_grant_type": "password",
                "redirect_uris": "",
            }
            application = Application.objects.create(**data)

        # if not Application.objects.all().exists():
        #     admin = User.objects.get(email="admin@addressbook.com", user_type="su")
        #     application = Application()
        #     application.name = "Backend"
        #     application.user_id = admin
        #     application.client_type = "confidential"
        #     application.authorization_grant_type = "password"
        #     application.redirect_uris = ""

        #     application.save()

        else:

            application = Application.objects.all().first()
        return application.client_id, application.client_secret
