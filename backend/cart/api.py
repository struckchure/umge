from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from umge.base import BaseAPIView as BaseView
from umge.payment import PaymentAPI
from cart.serializers import (
    CartSerializer,
    CartCreateSerializer,
    CartUpdateSerializer,
    CheckoutSerializer,
    CartItemUpdateSerializer
)
from cart.models import Cart


class CartCreate(BaseView):

    permission_classes = [
        IsAuthenticated
    ]
    serializer_class = CartCreateSerializer

    def post(self, request, *args, **kwargs):
        payload = request.data
        serialized_data = self.get_serializer(data=payload)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()

        response = Response(
            serialized_data.data,
            status=status.HTTP_200_OK
        )

        return response


class CartDetails(BaseView):

    permission_classes = [
        IsAuthenticated
    ]
    serializer_class = CartSerializer

    def get(self, request):
        cart_user = request.user
        user_cart, created = Cart.objects.get_or_create(cart_user=cart_user)

        if not created:
            user_cart.save()

        serialized_data = self.get_serializer(user_cart)

        response = Response(
            serialized_data.data,
            status=status.HTTP_200_OK
        )

        return response


class CartUpdate(BaseView):

    permission_classes = [
        IsAuthenticated
    ]
    serializer_class = CartUpdateSerializer

    def post(self, request, *args, **kwargs):
        cart_user = request.user
        user_cart, created = Cart.objects.get_or_create(cart_user=cart_user)

        if not created:
            user_cart.save()

        payload = request.data

        serialized_data = self.get_serializer(
            user_cart,
            data=payload
        )
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()

        serialized_data = serialized_data.data

        response = Response(
            serialized_data,
            status=status.HTTP_200_OK
        )

        return response


class Checkout(BaseView):

    permission_classes = [
        IsAuthenticated
    ]
    serializer_class = CheckoutSerializer

    def post(self, requests, *args, **kwargs):
        user = requests.user
        payload = requests.data

        serialized_data = self.get_serializer(data=payload)
        serialized_data.is_valid(raise_exception=True)

        user_cart = Cart.objects.get(cart_user=user)
        check_out = user_cart.check_out(serialized_data.data['payment_mode'])

        if check_out['status']:
            response = Response(
                check_out,
                status=status.HTTP_200_OK
            )
        else:
            response = Response(
                check_out,
                status=status.HTTP_402_PAYMENT_REQUIRED
            )

        return response


class BuyNow(BaseView):

    permission_classes = [
        IsAuthenticated
    ]
    serializer_class = CartItemUpdateSerializer

    def post(self, requests):
        user = requests.user
        payload = requests.data

        # location = {
        #     'latitude': '',
        #     'longitude': ''
        # }

        serialized_data = self.get_serializer(data=payload)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()

        buy_now_item = serialized_data.instance

        user_cart = Cart.objects.get(cart_user=user)
        check_out = user_cart.buy_now(
            item=buy_now_item,
            payment_mode=payload['payment_mode'],
            # location=location
        )

        if check_out['status']:
            response = Response(
                check_out,
                status=status.HTTP_200_OK
            )
        else:
            response = Response(
                check_out,
                status=status.HTTP_402_PAYMENT_REQUIRED
            )

        return response


class VerifyPayment(BaseView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, requests, reference):
        payment_api = PaymentAPI()
        verification = payment_api.verify(reference)

        response = Response(
            verification,
            status=status.HTTP_200_OK
        )

        return response
