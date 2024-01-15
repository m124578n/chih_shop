from account.models import Account
from rest_framework import serializers


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