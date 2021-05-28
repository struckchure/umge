from rest_framework import serializers

from locations.models import PickUpLocation, Region
from cart.models import Cart


class PickUpLocationSerializer(serializers.ModelSerializer):

    location_region = serializers.SerializerMethodField()

    class Meta:
        model = PickUpLocation
        fields = '__all__'

    def get_location_region(self, obj):
        return RegionSerializer(obj.get_region()).data


class RegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Region
        fields = '__all__'


class UpdatePickUpLocationSerializer(serializers.ModelSerializer):

	class Meta:
		model = Cart
		fields = [
			'cart_location'
		]
