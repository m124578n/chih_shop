from account.models import Account
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password


class AccountCreateSerializer(serializers.HyperlinkedModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = Account.objects.create_user(
                username=validated_data['username'],
                password=validated_data['password'],
                sex=validated_data['sex'],
                email=validated_data['email'],
                phone=validated_data['phone'],
                address=validated_data['address'],
                is_superuser=validated_data['is_superuser'],
                is_staff=validated_data['is_staff'],
            )
        return user

    class Meta:
        model = Account
        fields = ["username", "password", "sex", "email", "phone", "address", "url", "is_superuser", "is_staff"]



class AccountSerializer(serializers.HyperlinkedModelSerializer):

    sex = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = ["username", "sex", "email", "phone", "address", "url", "is_superuser", "is_staff"]

    def get_sex(self, obj):
        return obj.get_sex_display()
    

class ChangePasswordSerializer(serializers.Serializer):
    model = Account
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    class Meta:
        model = Account
        fields = ["old_password", "new_password"]
