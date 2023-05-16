from django.contrib import admin
from .models import Account, Post, Comment

# Register your models here.
admin.site.register(Account)
admin.site.register(Post)
admin.site.register(Comment)