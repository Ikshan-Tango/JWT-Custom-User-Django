from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser,PermissionsMixin

from .managers import CustomUserManager
# Create your models here.

class CustomUser(AbstractBaseUser,PermissionsMixin):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200,unique=True)
    password=models.CharField(max_length=200)

    is_staff = models.BooleanField(default=False, verbose_name='Staff account is activated')
    is_active = models.BooleanField(default=True, verbose_name='account is activated')
    is_admin = models.BooleanField(default=False, verbose_name='staff account')

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ()

    # def create_superuser(self, email, password, **extra_fields):
    #     """
    #     Creates and saves a superuser with the given email and password.
    #     """
    #     user=self._create_user(email, password, True, True, **extra_fields)
    #     user.save(using=self._db)
    #     return user

    # @property
    # def is_staff(self):
    #     "Is the user a member of staff?"
    #     # Simplest possible answer: All admins are staff
    #     return self.is_admin

    def __str__(self):
        return self.name

