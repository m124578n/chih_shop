from django.contrib import admin
from cart.models import Cart, CartHistory
# Register your models here.

admin.site.register(Cart)
admin.site.register(CartHistory)

