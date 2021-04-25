from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model, authenticate, login, logout

from umge.base import BaseAPIView as BaseView
from accounts.serializers import (
    UserRegisterSerializer,
    UserLoginSerializer,
    UserSerializer,
    WalletSerializer,
    UserUpdateSerializer
)
from store.serializers import StoreSerializer
from cart.serializers import CartSerializer


User = get_user_model()


class UserDetails(BaseView):

    serializer_class = UserSerializer
    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username=request.user.username)
        context = {
            'stores': StoreSerializer(user.get_stores(), many=True).data,
            'wallet': WalletSerializer(user.get_wallet()).data,
            'cart': CartSerializer(user.get_cart()).data
        }

        serialized_data = self.get_serializer(user).data

        response = Response(
            {
                **serialized_data,
                **context
            },
            status=status.HTTP_200_OK
        )

        return response


class UserRegister(BaseView):
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        payload = request.data
        serialized_data = self.get_serializer(data=payload)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()

        password = serialized_data.data.get('password')
        user = User(**serialized_data.data)
        user.set_password(password)
        user.save()

        token = Token.objects.create(user=user)

        response = Response(
            {
                'user': serialized_data.data,
                'token': token.key
            },
            status=status.HTTP_200_OK
        )

        return response


class UserLogin(BaseView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        payload = request.data
        serialized_data = self.get_serializer(data=payload)
        serialized_data.is_valid(raise_exception=True)

        user = authenticate(**serialized_data.data)

        if user:
            login(request, user)

            user = User.objects.get(username=request.user.username)
            token, created = Token.objects.get_or_create(user=user)

            response = Response(
                {
                    'user': UserSerializer(user).data,
                    'token': token.key
                },
                status=status.HTTP_200_OK
            )
        else:
            response = Response(
                {
                    'user': 'invalid credentials'
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

        return response


class UserLogout(BaseView):
    def get(self, request, *args, **kwargs):
        logout(request)

        return Response(
            {'user': 'logged out'},
            status=status.HTTP_200_OK
        )


class UserUpdate(BaseView):

    permission_classes = [
        IsAuthenticated
    ]
    serializer_class = UserUpdateSerializer

    def post(self, request, *args, **kwargs):
        payload = request.data
        user = request.user

        serialized_data = self.get_serializer(user, data=payload)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()

        response = Response(
            serialized_data.data,
            status=status.HTTP_200_OK
        )

        return response
