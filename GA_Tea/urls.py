from rest_framework.routers import SimpleRouter
from .views import AccountViewSet, LoginViewSet, RegistrationViewSet, RefreshViewSet, PostViewSet, CommentViewSet

routes = SimpleRouter()

routes.register(r'auth/login', LoginViewSet, basename='auth-login')
routes.register(r'auth/register', RegistrationViewSet, basename='auth-register')
routes.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')

routes.register(r'users', AccountViewSet, basename='users')

routes.register(r'posts', PostViewSet, basename='posts')
routes.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = [
    *routes.urls,
]