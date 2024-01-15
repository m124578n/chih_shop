from rest_framework import viewsets
from rest_framework import permissions
from shop.models import Product
from shop.serializers import ProductSerializer
from shop.permissions import IsOwnerPermission
from django.shortcuts import render

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by("id")
    serializer_class = ProductSerializer

    any_allow_actions = ['list', 'retrieve']

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in self.any_allow_actions:
            permission_classes = []
        else:
            permission_classes = [IsOwnerPermission]
        return [permission() for permission in permission_classes]
