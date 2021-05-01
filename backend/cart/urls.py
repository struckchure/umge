from django.urls import path

from cart.api import (
    CartCreate,
    CartDetails,
    CartUpdate,

    Checkout,
    BuyNow,
    VerifyPayment
)

app_name = 'cart'

urlpatterns = [
    path('cart/create/', CartCreate.as_view()),
    path('cart/details/', CartDetails.as_view()),
    path('cart/update/', CartUpdate.as_view()),

    path('cart/checkout/', Checkout.as_view()),
    path('cart/buy-now/', BuyNow.as_view()),
    path('payment/vefify/<slug:reference>/', VerifyPayment.as_view())
]
