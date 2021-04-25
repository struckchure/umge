from django.urls import path

from delivery.api import OrderList


urlpatterns = [
    path('delivery/orders/', OrderList.as_view())
]
