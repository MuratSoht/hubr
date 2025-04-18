from django.db import models
from users.models import 

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название поста')
    text = models.CharField(max_length=1_000_000, verbose_name='Содержание поста')
    author = 