from django.contrib.auth import get_user_model

from django.contrib.gis.db import models
from django.contrib.gis.geos import Point


USER_MODEL = get_user_model()


class Area(models.Model):
    name = models.CharField(max_length=100)
    region = models.MultiPolygonField()
    owner = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.name

    @staticmethod
    def search_by_lat_lng(lat, lng):
        point = Point(float(lat), float(lng))
        return Area.objects.filter(region__contains=point)
