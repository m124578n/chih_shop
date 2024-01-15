from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, permissions, status
from rest_framework.generics import (
    CreateAPIView, 
    UpdateAPIView,
    )
from rest_framework.views import APIView

from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout
from account.models import Account
from account.serializers import (
    AccountSerializer, 
    AccountCreateSerializer,
    ChangePasswordSerializer,
    )
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


class ChangePasswordView(UpdateAPIView):
        """
        An endpoint for changing password.
        """
        serializer_class = ChangePasswordSerializer
        model = Account
        permission_classes = (permissions.IsAuthenticated,)

        def get_object(self, queryset=None):
            obj = self.request.user
            return obj

        def update(self, request, *args, **kwargs):
            self.object = self.get_object()
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                # Check old password
                if not self.object.check_password(serializer.data.get("old_password")):
                    return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
                # set_password also hashes the password that the user will get
                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()
                response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'Password updated successfully',
                    'data': []
                }

                logout(request)

                return Response(response)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
