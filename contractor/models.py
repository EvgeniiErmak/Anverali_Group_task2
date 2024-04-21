# contractor/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser


class Contractor(AbstractUser):
    contact_info = models.TextField()
    experience = models.TextField()

    def __str__(self):
        return self.username
