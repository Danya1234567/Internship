from django.contrib.auth.models import AbstractUser
from django.db import models as m

# Create your models here.

class User(AbstractUser):
    username=m.CharField(max_length=50,unique=True)
    email=m.EmailField(max_length=300)
    password=m.CharField(max_length=128)
    created_at=m.DateTimeField(auto_now_add=True)
    verified=m.BooleanField(default=False)
    def __str__(self):
        return self.username