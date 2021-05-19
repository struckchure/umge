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
        order_list = Order.objects.filter(user=user).order_by('-date')

        serializer_data = self.get_serializer(order_list, many=True).data
        response = Response(
            serializer_data,
            status=status.HTTP_200_OK
        )

        return response


class RiderOrderList(BaseView):

    permission_classes = [
        IsAuthenticated,
        IsStaff
    ]
    queryset = Order.objects.order_by('-updated')

    def get(self, request):
        group_qs = group_rider_orders(self.get_queryset())
        response = Response(
            group_qs,
            status=status.HTTP_200_OK
        )

        return response


class RiderOrderAccept(BaseView):

    permission_classes = [
        IsAuthenticated,
        IsStaff
    ]

    def get(self, request, username):
        rider = User.objects.get(username=request.user.username)
        user = get_object_or_404(User, username=username)

        delivery = rider.make_delivery(user)

        if delivery['status']:
            status_code = status.HTTP_200_OK
        else:
            status_code = status.HTTP_400_BAD_REQUEST

        response = Response(
            delivery,
            status=status_code
        )
        
        return response
