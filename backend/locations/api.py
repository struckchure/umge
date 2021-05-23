from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from ipware import get_client_ip

from umge.base import BaseAPIView as BaseView
from accounts.permissions import IsStaff
from locations.models import PickUpLocation, Region
from locations.serializers import PickUpLocationSerializer, RegionSerializer


class CreateRegion(BaseView):

    permission_classes = [
        IsAuthenticated,
        IsStaff
    ]
    serializer_class = RegionSerializer

    def post(self, request):
        data = request.data

        serialized_data = self.get_serializer(data=data)
        serialized_data.is_valid(raise_exception=True)

        response = Response(
            serialized_data.data,
            status=status.HTTP_200_OK
        )

        return response


class RegionsList(BaseView):

    serializer_class = RegionSerializer
    queryset = Region.objects.order_by('-date')

    def get(self, request):
        serialized_data = self.get_serializer(self.get_queryset(), many=True).data

        response = Response(
            serialized_data,
            status=status.HTTP_200_OK
        )

        return response


class SaveCurrentLocation(BaseView):

    permission_classes = [
        IsStaff,
        IsAuthenticated
    ]
    serializer_class = PickUpLocationSerializer

    def post(self, request):
        data = request.data

        serialized_data = self.get_serializer(data=data)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()

        response = Response(
            serialized_data.data,
            status=status.HTTP_200_OK
        )

        return response

    def get(self, request):
        client_ip, is_routable = get_client_ip(request)

        response = Response(
            {
                'ip_address': client_ip,
                'is_routable':is_routable
            },
            status=status.HTTP_200_OK
        )

        return response


class LocationsList(BaseView):

    queryset = PickUpLocation.objects.order_by('-date')
    serializer_class = PickUpLocationSerializer

    def get(self, request):
        serialized_data = self.get_serializer(self.get_queryset(), many=True).data

        response = Response(
            serialized_data,
            status=status.HTTP_200_OK
        )

        return response

