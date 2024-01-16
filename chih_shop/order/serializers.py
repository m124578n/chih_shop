from rest_framework import serializers
from order.models import Order, OrderHistory


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Order
        fields = "__all__"
