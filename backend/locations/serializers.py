from rest_framework import serializers

from locations.models import PickUpLocation, Region


class PickUpLocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = PickUpLocation
        exclude = [
            'id'
        ]


class RegionSerializer(serializers.ModelSerializer):

	class Meta:
		model = Region
		exclude = [
			'id'
		]
