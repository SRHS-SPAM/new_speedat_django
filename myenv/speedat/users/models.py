from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=255)         #사용자 이름 최대 길이 255
    email = models.CharField(max_length=255, unique= True)      #사용자 이메일 최대 길이 255, 고유 값
    password = models.CharField(max_length=255)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []