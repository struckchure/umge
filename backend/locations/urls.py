from django.urls import path

from locations.api import (
	SaveCurrentLocation
)

app_name = 'locations'

urlpatterns = [
	path('locations/save-current-location/', SaveCurrentLocation.as_view())
]
