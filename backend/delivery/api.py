from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from umge.base import BaseAPIView as BaseView
from accounts.models import User
from accounts.permissions import IsStaff
from delivery.models import Order
from delivery.serializers import OrderSerializer
from delivery.utils import group_rider_orders


class OrderList(BaseView):

    permission_classes = [
        IsAuthenticated
    ]
    serializer_class = OrderSerializer

    def get(self, request, *args, **kwargs):
        user = request.user
        order_list = Order.objects.filter(
            user=user
        ).order_by('-date')

        serializer_data = self.get_serializer(order_list, many=True).data

        response = Response(
            serializer_data,
            status=status.HTTP_200_OK
        )

        return response
