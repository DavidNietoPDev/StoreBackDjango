from django.db import models
from django.contrib.auth.models import AbstractUser



class JSONFileField(models.FileField):
    def __init__(self, **kwargs):
        kwargs['upload_to'] = 'media/jsons'
        super().__init__(**kwargs)

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='media/products/images/')
    stock = models.IntegerField()
    category = models.CharField(max_length=255)
    actual_price = models.DecimalField(max_digits=10, decimal_places=2)
    history_price_dates_3years = JSONFileField(default=dict)  # Assume this stores a dictionary of dates and prices
    prediction_price_date = models.JSONField(default=dict, blank=True)  # Assume this stores a dictionary of future dates and predicted prices

    def __str__(self):
        return self.name

class User(AbstractUser):
    mail = models.EmailField(unique=True)
    role = models.CharField(max_length=255)
    history_buys = models.JSONField(default=list)  # Assume this stores a list of past purchases
    list_buy_in_shopping_cart = models.JSONField(default=list)  # Assume this stores a list of current items in the cart

    def __str__(self):
        return self.username
    
