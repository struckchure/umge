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
    UserUpdateSerializer,
    FundHistorySerializer,
    FundWalletSerializer
)
from store.serializers import StoreSerializer
from cart.serializers import CartSerializer
from accounts.models import (
    Wallet,
    FundHistory
)


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


class FundWallet(BaseView):

    permission_classes = [
        IsAuthenticated
    ]
    serializer_class = FundWalletSerializer

    def post(self, request):
        payload = request.data
        wallet = Wallet.objects.get(wallet_user=request.user)

        serialized_data = self.get_serializer(data=payload)
        serialized_data.is_valid(raise_exception=True)

        amount = serialized_data.validated_data.get('amount')
        fund_request = wallet.fund_wallet(amount)

        response = Response(
            fund_request,
            status=status.HTTP_200_OK
        )

        return response


class FundHistoryList(BaseView):

    permission_classes = [
        IsAuthenticated
    ]
    serializer_class = FundHistorySerializer

    def get(self, request):
        histories = FundHistory.objects.filter(user=request.user)\
            .order_by('-date')
        serialized_data = self.get_serializer(histories, many=True)

        response = Response(
            serialized_data.data,
            status=status.HTTP_200_OK
        )

        return response


class FundVerify(BaseView):

    permission_classes = [
        IsAuthenticated
    ]
    serializer_class = FundHistorySerializer

    def get(self, request):
        fund_history = FundHistory.objects.filter(
            user=request.user
        ).last()

        fund_history.verify_transaction()

        serialized_data = self.get_serializer(fund_history).data

        response = Response(
            serialized_data,
            status=status.HTTP_200_OK
        )

        return response
