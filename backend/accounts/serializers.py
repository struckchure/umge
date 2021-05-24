from rest_framework import serializers

from django.contrib.auth import get_user_model
from accounts.models import (
    Wallet,
    FundHistory
)


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = [
            'user_permissions',
            'groups',
            'password'
        ]


class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = [
            'groups',
            'user_permissions',
            'is_staff',
            'is_active',
            'last_login'
        ]

    def validate(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')

        email_qs = User.objects.filter(email=email)
        username_qs = User.objects.filter(username=username)

        if email_qs.exists():
            message = f'A user is already registered with email {email}'
            raise serializers.ValidationError(message)

        if username_qs.exists():
            message = f'Username {username} is already taken, try something else'
            raise serializers.ValidationError(message)

        return validated_data


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class WalletSerializer(serializers.ModelSerializer):

    class Meta:
        exclude = ['id']
        model = Wallet


class UserUpdateSerializer(serializers.ModelSerializer):

    password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=False)
    confirm_password = serializers.CharField(required=False)

    class Meta:
        model = User
        exclude = [
            'date',
            'updated'
        ]

    def validate(self, validated_data):
        return validated_data


class FundWalletSerializer(serializers.Serializer):

    amount = serializers.IntegerField()


class FundHistorySerializer(serializers.ModelSerializer):

    description = serializers.SerializerMethodField()
    amount = serializers.SerializerMethodField()

    class Meta:
        model = FundHistory
        fields = [
            'id',
            'user',
            'description',
            'amount',
            'date',
            'updated'
        ]

    def get_description(self, obj):
        return obj.get_description()

    def get_amount(self, obj):
        return obj.get_amount()
