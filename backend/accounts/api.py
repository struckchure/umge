from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model, authenticate, login, logout

from umge.base import BaseAPIView as BaseView
from accounts.serializers import (
    UserRegisterSerializer,
    UserLoginSerializer,
    UserSerializer
)


User = get_user_model()


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

            user = User.objects.get(username=payload['username'])
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
