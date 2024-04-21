# customer/models.py

from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    contact_info = models.TextField()
    experience = models.TextField()

    def __str__(self):
        return self.user.username
