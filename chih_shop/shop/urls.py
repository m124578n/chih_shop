from django.urls import path
from rest_framework import routers
from shop.views import ProductViewSet

router = routers.DefaultRouter()
router.register(r'', ProductViewSet)

urlpatterns = [
    
]


urlpatterns += router.urls
