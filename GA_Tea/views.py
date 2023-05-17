from .serializers import AccountSerializer, PostSerializer, CommentSerializer, LoginSerializer, RegisterSerializer
from .models import Account, Post, Comment
from django.shortcuts import render, get_object_or_404
from .permissions import IsOwnerOrReadOnly
from rest_framework import viewsets, permissions, generics, filters, status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
    
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]
    
    def perform_create(self, serializer):
      serializer.save(owner=self.request.user)
      
    def perform_update(self, serializer):
      serializer.save(owner=self.request.user)    

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]
    
    def perform_create(self, serializer):
      serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
      serializer.save(owner=self.request.user)   

class AccountViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'put', 'patch']
    # queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    filter_backends = [filters.OrderingFilter]
    authentication_classes = [JWTTokenUserAuthentication]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Account.objects.all()

    def get_object(self):
        lookup_field_value = self.kwargs[self.lookup_field]
        obj = Account.objects.get(id=lookup_field_value)
        self.check_object_permissions(self.request, obj)
        # auth_header = self.request.headers.get('Authorization')
        # print(auth_header, 'hello')

        return obj
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

class LoginViewSet(ModelViewSet, TokenObtainPairView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class RegistrationViewSet(ModelViewSet, TokenObtainPairView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
      try:
        user = Account.objects.get(username=request.data["username"])
      except Account.DoesNotExist:
        user = None
      if user == None :  
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        res = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
        return Response({
            "user": serializer.data,
            "refresh": res["refresh"],
            "access": res["access"]
        }, status=status.HTTP_201_CREATED)
      return HttpResponse("Account already exists")


class RefreshViewSet(viewsets.ViewSet, TokenRefreshView):
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)