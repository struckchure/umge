from django.urls import path
from django.http import HttpResponse

from store.api import (
    StoreList,
    StoreCreate,
    StoreDetails,
    StoreUpdate,

    ProductList,
    ProductCreate,

    ProductOptionCreate
)

app_name = 'store'

urlpatterns = [
    path('store/list/', StoreList.as_view()),
    path('store/create/', StoreCreate.as_view()),
    path('store/<slug:store_slug>/details/', StoreDetails.as_view()),
    path('store/<slug:store_slug>/update/', StoreUpdate.as_view()),

    path('product/list/<str:store_name>/<str:product_name>/', ProductList.as_view()),
    path('product/list/', ProductList.as_view()),
    path('product/create/', ProductCreate.as_view()),

    path('product/options/create/', ProductOptionCreate.as_view()),
]
