from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from umge.base import BaseAPIView as BaseView
from cart.serializers import (
    CartSerializer,
    CartCreateSerializer,
    CartUpdateSerializer
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

    def post(self, request):
        cart_user = request.user
        user_cart, created = Cart.objects.get_or_create(cart_user=cart_user)

        if not created:
            user_cart.save()

        serialized_data = CartSerializer(user_cart)

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
            data=payload,
            partial=True
        )
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()

        response = Response(
            serialized_data.data,
            status=status.HTTP_200_OK
        )

        return response
