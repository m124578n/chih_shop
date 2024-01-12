from django.db import models
from account.models import Account
from shop.models import Product
from cart.models import Cart, CartHistory
# Create your models here.

class Order(models.Model):

    owner = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name="owner"
        )
    
    shop = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name="shop"
        )
    
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE
        )
    
    item = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
        )
    
    quantity = models.IntegerField(
        verbose_name='quantity',
        default=1
        )
    
    def __str__(self):
        return self.id
    
    class Meta:
        db_table = 'order'



class OrderHistory(models.Model):

    owner = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name="history_owner"
        )
    
    shop = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name="history_shop"
        )
    
    cart = models.ForeignKey(
        CartHistory,
        on_delete=models.CASCADE
        )
    
    item_name = models.CharField(
        verbose_name='item_name',
        max_length=50
        )
    
    item_price = models.DecimalField(
        verbose_name='item_price',
        max_digits=8,
        decimal_places=0
        )
    
    order_quantity = models.IntegerField(
        verbose_name='order_quantity',
        default=1
        )
    
    amount = models.DecimalField(
        verbose_name='amount',
        max_digits=8,
        decimal_places=0
        )

    def __str__(self):
        return self.id
    
    class Meta:
        db_table = 'order_history'
