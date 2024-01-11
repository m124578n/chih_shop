from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import render, get_object_or_404
from .models import Account
# Create your views here.


@api_view(['GET'])
def test_create(request):
    user = request.user
    user = Account.objects.filter(username=user).first()
    return Response({'message': user.username})

