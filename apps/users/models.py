from functools import partial

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.users.managers import UserManager
from common.models import TimeStamped
from services.get_file_path import get_path_with_unique_filename


class CustomUser(AbstractBaseUser, PermissionsMixin, TimeStamped):
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        db_table = 'auth_user'
        verbose_name = _('user')
        verbose_name_plural = _('users')


class Profile(models.Model):
    # Regular expression for validating phone number in Ukraine
    phone_validator = RegexValidator(
        regex=r'^\+380[0-9]{9}',
        message='Enter phone in format +380XXXXXXXXX',
    )

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    phone = models.CharField(
        _('phone number'),
        validators=[phone_validator],
        max_length=25,
        blank=True,
    )
    avatar = models.ImageField(
        _('avatar'),
        upload_to=partial(get_path_with_unique_filename, file_path='images/users/avatars'),
        blank=True,
    )

    class Meta:
        db_table = 'user_profile'
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')
