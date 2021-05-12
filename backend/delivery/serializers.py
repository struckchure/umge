from rest_framework import serializers

from delivery.models import Order


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = [
        	'item',
			'transaction_id',
			'status',
			'date',
			'updated'
		]
        depth = 2
