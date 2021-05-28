from rest_framework import serializers

from cart.models import Cart
from delivery.models import Order, Delivery
from accounts.serializers import UserSerializer
from locations.serializers import PickUpLocationSerializer


class OrderSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    location = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = [
            'user',
            'item',
            'transaction_id',
            'location',
            'status',
            'date',
            'updated'
        ]
        depth = 2

    def get_location(self, obj):
        cart = Cart.objects.get(cart_user=obj.user)
        location = cart.get_cart_location()

        if location:
            return PickUpLocationSerializer(location).data

        return {}


class DeliverySerializer(serializers.ModelSerializer):

    rider = UserSerializer()
    reciepient = UserSerializer()
    location = serializers.SerializerMethodField()

    class Meta:
        model = Delivery
        exclude = [
            'id'
        ]
        depth = 1

    def get_location(self, obj):
        location = obj.get_delivery_location()

        if location:
            return PickUpLocationSerializer(location).data

        return {}
