from rest_framework import viewsets
from cart.serializers import CartSerializer
from cart.models import Cart

# Create your views here.


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all().order_by("id")
    serializer_class = CartSerializer
