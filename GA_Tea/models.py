from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin

class Hashtag(models.Model):
    tag = models.CharField()

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **kwargs):
        if username is None:
            raise TypeError('Need a Username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, email=None):
        if password is None:
            raise TypeError("Need Password")
        if username is None:
            raise TypeError("Need Username")
        user = self.create_user(username, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
    
class Account(AbstractUser, PermissionsMixin):
    bio = models.TextField(blank=True)
    github = models.CharField(default='', blank=True)
    linkedin = models.CharField(default='', blank=True)
    skills = ArrayField(models.CharField(max_length=200), default=list)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    pic = models.CharField(default='https://imgur.com/a/2L57GM9')

  
    objects = UserManager()

    def __str__(self):
        return self.username
    
class Post(models.Model):
    title = models.CharField(max_length=128, blank=True)
    body = models.TextField()
    pic = models.CharField(blank=True)
    skills = ArrayField(models.CharField(max_length=200), null=True, blank=True)
    # timeline = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = "posts", null=True)
    tag = models.ManyToManyField(Hashtag, blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    body = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = "comments", null=True)
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = "comments")
    
    def __str__(self):
        return self.owner.username

class Career(models.Model):
    company_name = models.CharField()
    status = models.CharField()
    timeline = models.DateTimeField()