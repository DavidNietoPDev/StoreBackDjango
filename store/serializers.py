from rest_framework import serializers
from .models import User, Product

class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(default="normal")
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'mail', 'role', 'history_buys', 'list_buy_in_shopping_cart']
        extra_kwargs = {
            'password': {'write_only': True},  # Make password write-only
            'history_buys': {'required': False, 'allow_null': True},
            'list_buy_in_shopping_cart': {'required': False, 'allow_null': True}
        }

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'image', 'stock', 'category', 'actual_price', 'history_price_dates_3years', 'prediction_price_date']
        extra_kwargs = {
            'history_price_dates_3years': {'required': False, 'allow_null':True},
            'prediction_price_date': {'required': False, 'allow_null': True}
        }
 

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'mail']
    
    def create(self, validated_data):
        user = User(
            username = validated_data['username'],
            mail = validated_data['mail']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user