from rest_framework import routers
from django.urls import path
from cart.views import CartViewSet

router = routers.DefaultRouter()
router.register(r'', CartViewSet)

urlpatterns = [
    
]

urlpatterns += router.urls

