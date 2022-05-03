import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from sequence.models import SequenceField
from safedelete.models import SafeDeleteModel, SOFT_DELETE_CASCADE
from django_countries.fields import CountryField


class UserManager(BaseUserManager):
    def get_by_natural_key(self, username, user_type):
        user_type = user_type if user_type else "su"
        return self.get(
            **{
                self.model.USERNAME_FIELD: username,
                "deleted__isnull": True,
                "user_type": user_type,
                "is_guest": False,
            }
        )


class TimestampMixin(models.Model):
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AbstractUser(AbstractBaseUser, PermissionsMixin, SafeDeleteModel, TimestampMixin):
    _safedelete_policy = SOFT_DELETE_CASCADE

    type_choices = (("su", "Super Admin"), ("anonymous", "Anonymous User"), ("normal", "Normal User"))
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    user_id = SequenceField(max_length=30, unique=True, db_index=True, prefix="USER", initial_value=1000)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    user_type = models.CharField(max_length=30, choices=type_choices, default="normal")
    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    is_staff = models.BooleanField(default=False)
    is_guest = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    objects = UserManager()

    USERNAME_FIELD = "email"

    @property
    def get_short_name(self):
        return self.email

    @property
    def allow_login(self):
        if self.is_active:
            return True
        else:
            return False

    class Meta:
        abstract = True
        app_label = "book"
        ordering = ["email"]
        unique_together = ("email", "deleted")


class AbstractAddress(SafeDeleteModel, TimestampMixin):
    _safedelete_policy = SOFT_DELETE_CASCADE

    type_choices = (("res", "Residential Address"), ("office", "Office Address "), ("others", "Other Address"))
    user = models.ForeignKey("book.User", on_delete=models.CASCADE)
    type = models.CharField(max_length=128, choices=type_choices, default="res")
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128, blank=True, null=True, default="")
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    zip = models.CharField(max_length=64)
    country = CountryField()
    phone = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        abstract = True
        app_label = "book"


class AbstractQueryLog(models.Model):
    query = models.TextField()
    ran_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        app_label = "book"
