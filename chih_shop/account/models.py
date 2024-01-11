from django.db import models

# Create your models here.

class Account(models.Model):
    
    class Sex(models.IntegerChoices):
        FEMALE = 1, "Female"
        MALE = 2, "Male"
        OTHER = 3, "Other"
    
    class Status(models.IntegerChoices):
        ACTIVATE = 1, "Activate"
        FREEZE = 2, "Freeze"
    
    name = models.CharField(
        verbose_name="name", 
        max_lenght=50
        )
    
    sex = models.PositiveSmallIntegerField(
        verbose_name="sex",
        choices=Sex,
        default=Sex.OTHER
        )
    
    phone = models.CharField(
        verbose_name="phone", 
        max_lenght=10
        )
    
    email = models.EmailField(
        verbose_name="email", 
        max_lenght=254
        )
    
    address = models.CharField(
        verbose_name="address", 
        max_lenght=100
        )
    
    status = models.PositiveSmallIntegerField(
        verbose_name="status",
        choices=Status,
        default=Status.ACTIVATE
        )
    
    def __str__(self):
        return self.name
    
    class Meta:
        de_table = 'account'