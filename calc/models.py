from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.db.models import expressions
from django.db.models.base import Model
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

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
        return self.nick


USER = get_user_model()

class History(models.Model):
    expression = models.CharField(_('expression'), max_length=400)
    result = models.CharField(_('result'), max_length=400)

    user = models.ForeignKey(USER, on_delete=models.CASCADE)

    def __str__(self):
        return self.expression + ' = ' + self.result
