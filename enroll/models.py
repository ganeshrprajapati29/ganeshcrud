from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100,blank=True, null=True)
def set_password(self, raw_password):
        self.password = make_password(raw_password)

def check_password(self, raw_password):
        return check_password(raw_password, self.password)