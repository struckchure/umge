from rest_framework import serializers

from cart.models import Cart
from store.models import Product
from accounts.serializers import UserSerializer
from store.serializers import ProductSerializer


class CartSerializer(serializers.ModelSerializer):
    cart_user = UserSerializer()
    cart_items = ProductSerializer(many=True)

    class Meta:
        model = Cart
        exclude = ['id']
        depth = 1


class CartCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        exclude = [
            'id',
            'cart_slug'
        ]


class CartItemUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            'product_slug',
            'product_options'
        ]


class CartUpdateSerializer(serializers.ModelSerializer):

    cart_items = ProductSerializer(many=True)

    class Meta:
        model = Cart
        fields = [
            'cart_items'
        ]

    def update(self, instance, validated_data):
        print(validated_data)

        instance.save()

        return instance
