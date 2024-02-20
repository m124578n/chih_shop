from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, permissions, status
from rest_framework.generics import (
    CreateAPIView, 
    UpdateAPIView,
    )
from rest_framework.views import APIView

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


class CreateAccountView(CreateAPIView):
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
    serializer_class = ChangePasswordSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # if using drf authtoken, create a new token 
        # if hasattr(user, 'auth_token'):
        #     user.auth_token.delete()
        # token, created = Token.objects.get_or_create(user=user)
        # return new token

        # TODO remove token or create new token with JWT
        logout(request)
        return Response({'message': 'change password successful'}, status=status.HTTP_200_OK)
    