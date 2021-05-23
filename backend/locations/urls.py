from django.urls import path

from locations.api import (
    SaveCurrentLocation,
    LocationsList,
    CreateRegion,
    RegionsList
)

app_name = 'locations'

urlpatterns = [
    path('locations/save-current-location/', SaveCurrentLocation.as_view()),
    path('locations/', LocationsList.as_view()),
    path('locations/regions/', RegionsList.as_view()),
    path('locations/regions/create/', CreateRegion.as_view())
]
