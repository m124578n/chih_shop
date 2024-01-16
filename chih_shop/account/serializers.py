from account.models import Account
from cart.models import Cart
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _


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
        ### change this to django signal
        # when account register, add a default shopping cart for him.
        # Cart.objects.create(
        #     name='default shopping cart',
        #     owner=user
        #     )
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
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(max_length=128, write_only=True, required=True)
    new_password1 = serializers.CharField(max_length=128, write_only=True, required=True)
    new_password2 = serializers.CharField(max_length=128, write_only=True, required=True)

    def validate_old_password(self, value):
        """
        rest_framework serializers.py 394 line explain that how validate_method works
        """
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError(
                _('Your old password was entered incorrectly. Please enter it again.')
            )
        return value

    def validate(self, data):
        if data['new_password1'] != data['new_password2']:
            raise serializers.ValidationError({'new_password2': _("The two password fields didn't match.")})
        # password_validation.validate_password(data['new_password1'], self.context['request'].user)
        return data

    def save(self, **kwargs):
        password = self.validated_data['new_password1']
        user = self.context['request'].user
        user.set_password(password)
        user.save()
        return user

