from django.urls import path

from locations.api import (
    SaveCurrentLocation,
    LocationsList,
    CreateRegion,
    RegionsList,

    UpdatePickUpLocation
)

app_name = 'locations'

urlpatterns = [
    path('locations/create/', SaveCurrentLocation.as_view()),
    path('locations/', LocationsList.as_view()),
    path('locations/regions/', RegionsList.as_view()),
    path('locations/regions/create/', CreateRegion.as_view()),

    path('locations/update-pickup-location/', UpdatePickUpLocation.as_view())
]
