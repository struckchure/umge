from django.urls import path

from locations.api import (
    SaveCurrentLocation,
    LocationsList
)

app_name = 'locations'

urlpatterns = [
    path('locations/save-current-location/', SaveCurrentLocation.as_view()),
    path('locations/', LocationsList.as_view())
]
