from django.contrib.postgres.fields import ArrayField
from PIL import Image
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser

class Hashtag(models.Model):
    tag = models.CharField()

class Account(AbstractBaseUser):
    username = models.CharField(max_length=128, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField()
    bio = models.TextField(blank=True)
    github = models.CharField(default='', blank=True)
    linkedin = models.CharField(default='', blank=True)
    skills = ArrayField(models.CharField(max_length=200), default=list)
    pic = models.CharField(default='https://imgur.com/a/2L57GM9')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return f'{self.username}'
    
class Post(models.Model):
    title = models.CharField(max_length=128, blank=True)
    body = models.TextField()
    likes = models.IntegerField()
    pic = models.CharField(blank=True)
    skills = ArrayField(models.CharField(max_length=200), default=list)
    # timeline = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = "posts")
    tag = models.ManyToManyField(Hashtag)

    def __str__(self):
        return f'{self.title}'

class Comment(models.Model):
    body = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = "comments")
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = "comments")
    
    def __str__(self):
        return f'{self.user}'