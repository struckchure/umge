from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from umge.base import BaseAPIView as BaseView
from accounts.models import User, Rider
from accounts.permissions import IsAdminUser
from accounts.serializers import UserSerializer


class AdminUserList(BaseView):

    permission_classes = [
        IsAdminUser,
        IsAuthenticated
    ]
    queryset = User.objects.order_by('-date')
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        serialized_data = UserSerializer(
            self.get_queryset(),
            many=True
        ).data

        response = Response(
            serialized_data,
            status=status.HTTP_200_OK
        )
        return response


class AdminRiderList(BaseView):

    permission_classes = [
        IsAdminUser,
        IsAuthenticated
    ]
    queryset = Rider.objects.order_by('-date')
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        serialized_data = UserSerializer(
            self.get_queryset(),
            many=True
        ).data

        response = Response(
            serialized_data,
            status=status.HTTP_200_OK
        )
        return response
