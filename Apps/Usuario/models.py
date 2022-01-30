from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    bio = models.TextField(blank=True)
    email = models.EmailField(verbose_name='email address',
                              max_length=254, unique=True, blank=False,
                              null=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
