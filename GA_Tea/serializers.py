from rest_framework import serializers
from .models import Account, Post, Comment
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.password_validation import validate_password

class PostSerializer(serializers.ModelSerializer):
  owner = serializers.CharField()
  class Meta:
    model = Post
    fields = '__all__'
    owner = serializers.ReadOnlyField(source='owner.username')
    
class CommentSerializer(serializers.ModelSerializer):
  owner = serializers.CharField()
  class Meta:
    model = Comment
    fields = '__all__'
    owner = serializers.ReadOnlyField(source='owner.username')

class AccountSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
    comments = serializers.PrimaryKeyRelatedField(many=True, queryset=Comment.objects.all())

    class Meta:
        model = Account
        fields = ['id', 'username', 'email', "bio", "github", "linkedin", "skills", "pic", "posts", "comments"]

class LoginSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['user'] = AccountSerializer(self.user).data
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data

class RegisterSerializer(AccountSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    username = serializers.CharField(max_length=128, required=True)
    email = serializers.CharField(max_length=128, required=True)

    class Meta:
        model = Account
        fields = ['id', 'username', 'email', 'pic', 'date_joined', 'password']

    def create(self, validated_data):
        try:
            user = Account.objects.get(username=validated_data['username'])
            user = None
        except ObjectDoesNotExist:
            user = Account.objects.create_user(**validated_data)
        return user