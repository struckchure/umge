from django.urls import path

from delivery.api import (
	RiderOrderList,
	RiderOrderAccept
)
from delivery.admin_api import (
    AdminOrderList
)

urlpatterns = [
    path('delivery/orders/', RiderOrderList.as_view()),
    path('delivery/orders/<str:username>/accept/', RiderOrderAccept.as_view()),

    path('delivery/admin/orders/', AdminOrderList.as_view())
]
