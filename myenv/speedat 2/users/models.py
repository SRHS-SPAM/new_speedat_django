from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    #사용자 이름 필드 최대 255
    name = models.CharField(max_length=255)
    #사용자 이메일 필드 최대 255, 고유함
    email = models.CharField(max_length=255, unique=True)
    #사용자 비번 필드 최대 255
    password = models.CharField(max_length=255)
    #유저이름 없음
    username = None

    #유저이름 필드 = 이메일 필드
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []