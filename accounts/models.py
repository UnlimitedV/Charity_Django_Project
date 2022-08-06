from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    choices = (
        ('F', 'female'),
        ('M', 'male')
    )
    address = models.TextField(blank=True, null=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    first_name = models.CharField(blank=True, null=True)
    gender = models.CharField(blank=True, null=True, max_length=1, choices=choices)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(blank=True, null=True)
    last_name = models.CharField(blank=True, null=True)
    phone = models.CharField(blank=True, null=True, max_length=15)
