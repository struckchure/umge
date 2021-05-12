from django.urls import path

from delivery.api import RiderOrderList
from delivery.admin_api import (
    AdminOrderList
)

urlpatterns = [
    path('delivery/orders/', RiderOrderList.as_view()),

    path('delivery/admin/orders/', AdminOrderList.as_view())
]
