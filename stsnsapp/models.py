from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone





#ゲストログイン
class CustomUser(AbstractUser):
    """拡張ユーザーモデル"""
    how_many_liquor = models.IntegerField(default=1)
    how_many_cigalettes = models.IntegerField(default=1)

    class Meta:
        verbose_name_plural = 'CustomUser'
class cigalettes(models.Model):
    how_many_cigalettes2 = models.IntegerField(default=0)
    user_cigalettes = models.ForeignKey(CustomUser, on_delete=models.CASCADE,default=1)

class liquor(models.Model):
    how_many_liquor2 = models.IntegerField(default=0)
    user_liquor = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True)


class BoardModel(models.Model):
    title = models.CharField(max_length=100,null=True,blank=True)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE,default=1)
    good = models.IntegerField(null=True,blank=True,default=0)
    date = models.DateTimeField(default=timezone.now)
