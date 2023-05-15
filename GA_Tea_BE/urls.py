from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from GA_Tea.views import UserViewSet, PostViewSet, CommentViewSet, ReplyViewSet, CareerViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'post', PostViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'reply', ReplyViewSet)
router.register(r'career', CareerViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls)
]