from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from umge.base import BaseAPIView as BaseView
from accounts.permissions import IsStaff
from delivery.models import Order
from delivery.serializers import OrderSerializer


class AdminOrderList(BaseView):

    permission_classes = [
        IsAuthenticated,
        IsStaff
    ]
    queryset = Order.objects.order_by('-date')
    serializer_class = OrderSerializer

    def get(self, requests):
        serialized_data = self.get_serializer(self.get_queryset(), many=True)
        response = Response(
            serialized_data.data,
            status=status.HTTP_200_OK
        )

        return response
