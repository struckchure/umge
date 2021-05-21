from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from ipware import get_client_ip

from umge.base import BaseAPIView as BaseView
from accounts.permissions import IsStaff


class SaveCurrentLocation(BaseView):

	permission_classes = [
		IsStaff,
		IsAuthenticated
	]

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
