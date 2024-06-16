from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .api import ProductViewSet, UserViewSet, UserRegistrationViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
router.register(r'register', UserRegistrationViewSet, 'register')


urlpatterns = [
    path('', include(router.urls)),
]