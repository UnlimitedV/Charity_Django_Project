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
    gender = models.CharField(blank=True, null=True, max_length=1, choices=choices)
    phone = models.CharField(blank=True, null=True, max_length=15)
