from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from django.db.models import CharField, EmailField
from django.utils.translation import ugettext_lazy as _

from drive.users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    name = CharField(_("Name of User"), blank=True, max_length=255)
    email = EmailField(
        _("email address"),
        unique=True,
        db_index=True,
        error_messages={"unique": _("A user with that email already exists.")},
    )

    USERNAME_FIELD = "email"

    objects = UserManager()

    class Meta:
        ordering = ["-date_joined"]
