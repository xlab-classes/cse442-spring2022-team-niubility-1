from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    mpassword = models.CharField(verbose_name='password', blank=True, null=True, default='0', max_length=100)
    mobile = models.CharField(verbose_name='phone number', blank=True, null=True, default='', max_length=100)
    email = models.CharField(verbose_name='email', blank=True, null=True, default='', max_length=100)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['-id']
        verbose_name = 'User Management'
        verbose_name_plural = verbose_name