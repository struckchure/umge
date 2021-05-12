from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from umge.base import BaseAPIView as BaseView
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
        IsAuthenticated
    ]
    queryset = Order.objects.order_by('-updated')

    def get(self, request):
        group_qs = group_rider_orders(self.get_queryset())
        response = Response(
            group_qs,
            status=status.HTTP_200_OK
        )

        return response
