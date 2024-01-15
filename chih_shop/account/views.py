from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, permissions, status
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView

from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout
from account.models import Account
from account.serializers import AccountSerializer, AccountCreateSerializer
# Create your views here.


@api_view(['GET'])
def test_check(request):
    user = request.user
    user = Account.objects.filter(username=user).first()
    return Response({'message': user.username})


class AccountsView(viewsets.ModelViewSet):
    queryset = Account.objects.all().order_by("id")
    permission_classes = [
        permissions.IsAuthenticated # Or anon users can't register
    ]
    serializer_class = AccountSerializer

    def create(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class CreateAccount(CreateAPIView):
    model = Account
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = AccountCreateSerializer


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "Logout successful"})
    