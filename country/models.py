from typing import List
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import GeoFunc
from django.contrib.postgres.fields import JSONField, ArrayField


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


class AdminLevelEntry(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    osm_id = models.BigIntegerField(blank=True, null=True, unique=True)
    osm_type = models.CharField(blank=True, null=True, max_length=100)
    name = models.CharField(max_length=1000, blank=True, null=True)
    properties = JSONField(default={}, blank=True, null=True)
    admin_level = models.PositiveIntegerField(blank=True, null=True)
    geometry = models.GeometryField(srid=4326)

    def __str__(self):
        return "{}, {}".format(
            self.country.name, self.admin_level
        )
