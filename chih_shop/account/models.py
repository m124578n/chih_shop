from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Account(AbstractUser):
    
    class Sex(models.IntegerChoices):
        FEMALE = 0, "Female"
        MALE = 1, "Male"
        OTHER = 2, "Other"
    
    sex = models.PositiveSmallIntegerField(
        verbose_name="sex",
        choices=Sex,
        default=Sex.OTHER
        )
    
    phone = models.CharField(
        verbose_name="phone", 
        max_length=10
        )
    
    email = models.EmailField(
        verbose_name="email", 
        max_length=254
        )
    
    address = models.CharField(
        verbose_name="address", 
        max_length=100
        )
    
    def __str__(self):
        return self.username
