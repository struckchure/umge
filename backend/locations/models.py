from django.db import models

from accounts.models import User


class Region(models.Model):
    region_author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    region = models.CharField(max_length=100, unique=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    date = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.region

    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regions"


class PickUpLocation(models.Model):
    location_author = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50, blank=False, unique=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    date = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Pick up location"
        verbose_name_plural = "Pick up locations"

    def get_point(self):
        return self.latitude, self.longitude

    def get_region(self):
        return self.region
