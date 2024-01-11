from django.db import models
from account.models import Account
# Create your models here.

class Product(models.Model):

    class Status(models.IntegerChoices):
        ON = 0, 'On Sale'
        OFF = 1, 'Off Sale'
    
    owner = models.ForeignKey(
        Account, 
        on_delete=models.CASCADE
        )

    name = models.CharField(
        verbose_name='name',
        max_length=50
        )
    
    price = models.DecimalField(
        verbose_name='price',
        max_digits=8,
        decimal_places=0
        )
    
    status = models.IntegerField(
        verbose_name='status',
        choices=Status,
        default=Status.ON
        )
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'product'
