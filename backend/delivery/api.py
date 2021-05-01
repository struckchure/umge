from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from umge.base import BaseAPIView as BaseView
from accounts.permissions import IsStaff
from delivery.models import Order
from delivery.serializers import OrderSerializer


class OrderList(BaseView):

    permission_classes = [
        IsAuthenticated,
        IsStaff
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
