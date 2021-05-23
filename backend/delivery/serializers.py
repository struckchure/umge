from rest_framework import serializers

from delivery.models import Order, Delivery
from accounts.serializers import UserSerializer


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


class DeliverySerializer(serializers.ModelSerializer):

	rider = UserSerializer()
	reciepient = UserSerializer()
	locaation = serializers.SerializerMethodField()

	class Meta:
		model = Delivery
		exclude = [
			'id'
		]
		depth = 1

	def get_location(self, obj):
		return obj.get_delivery_location()
