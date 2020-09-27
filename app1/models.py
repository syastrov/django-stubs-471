from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class AuthUser(PermissionsMixin, AbstractBaseUser):
    class Meta:
        abstract = False
        db_table = 'auth_user'
