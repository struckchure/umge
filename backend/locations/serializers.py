from rest_framework import serializers

from locations.models import PickUpLocation


class PickUpLocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = PickUpLocation
        exclude = [
            'id'
        ]
