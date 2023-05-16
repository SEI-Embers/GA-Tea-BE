from rest_framework import serializers
from .models import Account, Post, Comment
from django.contrib.auth import get_user_model


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = '__all__'

class AccountSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True)

    class Meta:
        model = get_user_model()
        fields = ("username", "email", "password", "bio", "github", "linkedin", "skills", "pic", "posts")