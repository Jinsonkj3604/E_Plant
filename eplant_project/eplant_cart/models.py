from django.db import models
from eplant_home.models import *

# Create your models here.
class CartList(models.Model):
    cart_id = models.CharField(max_length=200,unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    prod = models.ForeignKey(Product,on_delete=models.CASCADE)
    cart = models.ForeignKey(CartList,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)
    
    def totalsum(self):
        return self.prod.price*self.quantity
    