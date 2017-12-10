from typing import List
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import GeoFunc


class GeneratePoints(GeoFunc):
    function = 'ST_GeneratePoints'


class RandomPointMixin(object):
    def get_random_geometry_point(self) -> Point:
        points: List[Point] = self.__class__.objects.filter(id=self.id).annotate(  # type: ignore
            rand_point=GeneratePoints(
                'geometry',
                models.Value(1)  # type: Any
            )
        ).first().rand_point
        return points[0]


class Country(RandomPointMixin, models.Model):  # type: ignore
    name = models.CharField(
        max_length=255
    )
    iso_2_digit = models.CharField(
        max_length=2,
        unique=True
    )
    iso_3_digit = models.CharField(
        max_length=3,
        unique=True
    )
    geometry = models.MultiPolygonField(srid=4326)

    def __str__(self) -> str:
        return self.name
