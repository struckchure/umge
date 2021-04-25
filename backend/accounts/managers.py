from django.contrib.auth.base_user import BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError("Username not set")

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, username, password=True, **extra_fields):
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self._create_user(username, password, **extra_fields)

    def get_queryset(self, *args, **kwargs):
        from accounts.models import User

        qs = super().get_queryset(*args, **kwargs).filter(type=User.Types.NORMAL)
        return qs


class RiderManager(models.Manager):

    def get_queryset(self, *args, **kwargs):
        from accounts.models import User

        qs = super().get_queryset(*args, **kwargs).filter(type=User.Types.RIDER)
        return qs
