from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=100, verbose_name='Имя пользователя')
    email = models.EmailField(max_length=100, unique=True, verbose_name='Email')
    USERNAME_FIELD = 'email'
    avatar_photo = models.ImageField(upload_to='avatars/', default='avatars/default.png', verbose_name='Изображение пользователя', blank=True)
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    
    def get_absolute_url(self):
        return reverse('users:detail_user', args=(self.id, ))
    
