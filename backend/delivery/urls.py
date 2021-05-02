from django.urls import path

from delivery.api import OrderList
from delivery.admin_api import (
    AdminOrderList
)

urlpatterns = [
    path('delivery/orders/', OrderList.as_view()),

    path('delivery/admin/orders/', AdminOrderList.as_view())
]
