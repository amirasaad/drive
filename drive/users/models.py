from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from django.db.models import EmailField, DateTimeField, BooleanField
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from drive.users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    email = EmailField(
        _("email address"),
        unique=True,
        db_index=True,
        error_messages={"unique": _("A user with that email already exists.")},
    )
    # Copied from
    date_joined = DateTimeField(_('date joined'), default=timezone.now)

    is_active = BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    is_staff = BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )

    USERNAME_FIELD = "email"

    objects = UserManager()

    class Meta:
        ordering = ["-date_joined"]
