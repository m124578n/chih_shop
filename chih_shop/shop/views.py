from rest_framework import viewsets
from rest_framework import permissions
from shop.models import Product
from shop.serializers import ProductSerializer, CreateProductSerializer
from shop.permissions import IsOwnerPermission
from django.shortcuts import render

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by("id")
    serializer_class = ProductSerializer
    permission_classes = [IsOwnerPermission, permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateProductSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)    
