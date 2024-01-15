from rest_framework import serializers
from shop.models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):

    status_display_value = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Product
        fields = ["name", "price", "status", "status_display_value", "url", "owner"]



class CreateProductSerializer(serializers.HyperlinkedModelSerializer):

    status_display_value = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Product
        fields = ["name", "price", "status", "status_display_value", "url"]
    