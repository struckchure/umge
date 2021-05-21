from django.urls import path

from delivery.api import (
    OrderList
)
from delivery.admin_api import (
    AdminOrderList
)
from delivery.riders_api import (
    RiderDeliveryList,
    RiderTasks,
    RiderOrderList,
    RiderOrderAccept,
    RiderDeliveryDone
)

urlpatterns = [
    path('delivery/riders/deliveries/', RiderDeliveryList.as_view()),
    path('delivery/riders/tasks/', RiderTasks.as_view()),
    path('delivery/riders/tasks/<str:delivery_status>/', RiderTasks.as_view()),
    path('delivery/riders/tasks/<slug:delivery_slug>/finish/', RiderDeliveryDone.as_view()),
    path('delivery/riders/orders/<str:username>/accept/', RiderOrderAccept.as_view()),

    path('delivery/orders/', OrderList.as_view()),

    path('delivery/admin/orders/', AdminOrderList.as_view())
]
