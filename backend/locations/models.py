from django.db import models
from django.contrib.gis.geos import Point

from accounts.models import User


class PickUpLocation(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=False, unique=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    date = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Pick up location'
        verbose_name_plural = 'Pick up locations'

    def get_point(self):
        point = Point(self.latitude, self.longitude)

        return point
