from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from umge.base import BaseAPIView as BaseView
from accounts.permissions import IsStaff
from store.models import (
    Store,
    Product
)
from store.serializers import (
    StoreSerializer,
    StoreCreateSerializer,
    StoreUpdateSerializer,

    ProductSerializer,
    ProductCreateSerializer,
    ProductOptionCreateSerializer
)


class StoreMain(BaseView):

    permission_classes = [
        IsAuthenticated
    ]
    serializer_class = StoreSerializer

    def get(self, request, *args, **kwargs):
        user = request.user
        store = Store.objects.filter(store_owner=user)
        serialized_data = self.get_serializer(store, many=True).data

        response = Response(
            serialized_data,
            status=status.HTTP_200_OK
        )

        return response


class StoreCreate(BaseView):

    serializer_class = StoreCreateSerializer
    permission_classes = [
        IsAuthenticated,
        IsStaff
    ]

    def post(self, request, *args, **kwargs):
        payload = request.data
        serialized_data = self.get_serializer(data=payload)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()

        response = Response(
            serialized_data.data,
            status=status.HTTP_200_OK
        )

        return response


class StoreUpdate(BaseView):

    serializer_class = StoreUpdateSerializer
    permission_classes = [
        IsAuthenticated,
        IsStaff
    ]

    def post(self, request, store_slug):
        store = get_object_or_404(Store, store_slug=store_slug)
        payload = request.data

        serialized_data = self.get_serializer(store, data=payload)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()

        response = Response(
            serialized_data.data,
            status=status.HTTP_200_OK
        )

        return response


class StoreDetails(BaseView):

    serializer_class = StoreSerializer

    def get(self, request, store_slug):
        store = get_object_or_404(Store, store_slug=store_slug)
        serialized_data = self.get_serializer(store).data

        response = Response(
            serialized_data,
            status=status.HTTP_200_OK
        )

        return response


class StoreList(BaseView):

    queryset = Store.objects.order_by('updated')
    serializer_class = StoreSerializer

    def get(self, request, *args, **kwargs):
        serialized_data = self.get_serializer(
            self.get_queryset(),
            many=True
        ).data

        response = Response(serialized_data)

        return response


class StoreProductList(BaseView):

    queryset = Product.objects.order_by('-updated')
    serializer_class = ProductSerializer

    def get(self, request, store_slug, *args, **kwargs):
        store = get_object_or_404(Store, store_slug=store_slug)
        products = Product.objects.filter(product_store=store)
        serialized_data = self.get_serializer(products, many=True).data

        response = Response(
            serialized_data,
            status=status.HTTP_200_OK
        )
        return response


class ProductList(BaseView):

    serializer_class = ProductSerializer
    queryset = Product.objects.order_by('-updated')

    def get(self, request, store_name="", product_name=""):
        if store_name == "*":
            store_name = ''

        if product_name == "*":
            product_name = ''

        queryset = Product.objects.filter(
            product_store__store_name__contains=store_name,
            product_name__contains=product_name
        ).order_by('-updated')
        serialized_data = self.get_serializer(queryset, many=True)

        response = Response(
            serialized_data.data,
            status=status.HTTP_200_OK
        )

        return response


class ProductCreate(BaseView):

    serializer_class = ProductCreateSerializer
    permission_classes = [
        IsAuthenticated,
        IsStaff
    ]

    def post(self, request, *args, **kwargs):
        payload = request.data
        serialized_data = self.get_serializer(data=payload)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()

        response = Response(
            serialized_data.data,
            status=status.HTTP_200_OK
        )
        return response


class ProductOptionCreate(BaseView):

    serializer_class = ProductOptionCreateSerializer
    permission_classes = [
        IsAuthenticated,
        IsStaff
    ]

    def post(self, request, *args, **kwargs):
        payload = request.data
        serialized_data = self.get_serializer(data=payload)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()

        response = Response(
            serialized_data.data,
            status=status.HTTP_200_OK
        )
        return response
