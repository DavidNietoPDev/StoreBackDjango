from .models import User, Product
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
   queryset = Product.objects.all()
   permission_classes = [permissions.AllowAny]
   serializer_class = ProductSerializer

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer