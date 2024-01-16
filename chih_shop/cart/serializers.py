from rest_framework import serializers
from cart.models import Cart, CartHistory
from order.serializers import OrderSerializer


class CartSerializer(serializers.HyperlinkedModelSerializer):

    orders = OrderSerializer(many=True, source='order_set')
    
    class Meta:
        model = Cart
        fields = "__all__"
