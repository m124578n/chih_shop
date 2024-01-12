from django.db import models
from account.models import Account

# Create your models here.

class Cart(models.Model):

    class Status(models.IntegerChoices):
        WAIT = 0, 'wait for ordering'
        GOING = 1, 'handle the order'
        SUCCESS = 2, 'success all order'
        FAIL = 3, 'fail some wrong'
        CANCEL = 4, 'cancel the order'

    name = models.CharField(
        verbose_name='name',
        max_length=50
        )

    owner = models.ForeignKey(
        Account,
        on_delete=models.CASCADE
        )
    
    created_at = models.DateTimeField(
        verbose_name='created_at',
        auto_now_add=True
        )
    
    status = models.PositiveSmallIntegerField(
        verbose_name='status',
        choices=Status,
        default=Status.WAIT
        )
    
    def __str__(self):
        return self.id
    
    class Meta:
        db_table = 'cart'


class CartHistory(models.Model):

    owner = models.ForeignKey(
        Account,
        on_delete=models.CASCADE
        )
    
    name = models.CharField(
        verbose_name='name',
        max_length=50
        )
    
    created_at = models.DateTimeField(
        verbose_name='created_at',
        auto_now_add=True
        )
    
    def __str__(self):
        return self.id
    
    class Meta:
        db_table = 'cart_history'
    
    