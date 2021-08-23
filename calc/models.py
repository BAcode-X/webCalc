from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    nick = models.CharField(_('nickname'), unique=True, max_length=200)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), null=True, max_length=200)
    last_name = models.CharField(_('last name'), null=True, max_length=200)

    USERNAME_FIELD = 'nick'
    REQUIRED_FIELDS = ['email',]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
