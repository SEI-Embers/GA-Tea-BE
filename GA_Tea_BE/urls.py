from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/', include(('GA_Tea.urls', 'ga_tea'), namespace='gatea-api')),
    
]