from rest_framework import serializers

from delivery.models import Order


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        exclude = [
            'id',
            'user'
        ]
        depth = 2
