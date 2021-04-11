from django.urls import path

from cart.api import (
    CartCreate,
    CartDetails,
    CartUpdate
)

app_name = 'cart'

urlpatterns = [
    path('cart/create/', CartCreate.as_view()),
    path('cart/details/', CartDetails.as_view()),
    path('cart/update/', CartUpdate.as_view())
]
