from rest_framework import serializers
from cart.models import Cart, CartHistory



class CartSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Cart
        fields = "__all__"
