from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, nick, email, password, first_name, last_name, **extra_fields):
        """
        Create and save a User with the given nickname, email and password.
        """
        if not nick:
            raise ValueError(_('The Nickname must be provided'))

        if not email:
            raise ValueError(_('The Email must be provided'))

        email = self.normalize_email(email)
        user = self.model(nick=nick, first_name=first_name, last_name=last_name, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, nick, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given nickname, email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if not nick:
            raise ValueError(_('The Nickname must be provided'))

        if not email:
            raise ValueError(_('The Email must be provided'))

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(nick, email, password,  first_name=None, last_name=None, **extra_fields)
