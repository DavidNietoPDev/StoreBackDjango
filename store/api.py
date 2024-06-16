from .models import User, Product
from rest_framework import mixins, viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, ProductSerializer, UserRegistrationSerializer
from .permissions import IsAdminOrReadOnly


class ProductViewSet(viewsets.ModelViewSet):
   queryset = Product.objects.all()
   permission_classes = [IsAdminOrReadOnly]
   serializer_class = ProductSerializer

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   permission_classes = [permissions.IsAdminUser]
   serializer_class = UserSerializer

class UserRegistrationViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)