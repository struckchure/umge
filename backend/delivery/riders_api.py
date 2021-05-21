from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from umge.base import BaseAPIView as BaseView
from accounts.permissions import IsStaff
from delivery.models import Delivery, Order
from delivery.serializers import DeliverySerializer


class RiderOrderList(BaseView):

    permission_classes = [
        IsAuthenticated,
        IsStaff
    ]
    queryset = Order.objects\
        .filter(status=Order.STATUS.PENDING)\
        .order_by('-updated')

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


class RiderDeliveryList(BaseView):

    permission_classes = [
        IsAuthenticated,
        IsStaff
    ]

    def get(self, request):
        deliveries = Delivery.objects.filter(rider=request.user)
        serialized_deliveries = DeliverySerializer(deliveries, many=True).data

        response = Response(
            serialized_deliveries,
            status=status.HTTP_200_OK
        )

        return response


class RiderTasks(BaseView):

    permission_classes = [
        IsStaff,
        IsAuthenticated
    ]

    def get(self, request, delivery_status='PD'):
        if delivery_status != "*":
            deliveries = Delivery.objects.filter(
                rider=request.user,
                status=delivery_status
            )
        else:
            deliveries = Delivery.objects.filter(
                rider=request.user
            )

        serialized_deliveries = DeliverySerializer(deliveries, many=True).data

        response = Response(
            serialized_deliveries,
            status=status.HTTP_200_OK
        )

        return response


class RiderDeliveryDone(BaseView):

    permission_classes = [
        IsAuthenticated,
        IsStaff
    ]

    def get(self, request, delivery_slug):
        delivery = get_object_or_404(Delivery, slug=delivery_slug)
        delivery.status = Delivery.STATUS.DONE
        delivery.save()

        serialized_delivery = DeliverySerializer(delivery).data

        response = Response(
            serialized_delivery,
            status=status.HTTP_200_OK
        )

        return response
