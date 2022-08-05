from pickle import NONE
from unicodedata import name
from django.db import models
import uuid

# Create your models here.
class Account(models.Model):
    id= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    role = models.CharField(max_length=32)

    def __str__(self):
        return self.username

