import factory
from django.contrib.gis.geos import MultiPolygon, Polygon

from country.models import Country


class CountryFactory(factory.DjangoModelFactory):
    name = 'Switzerland'
    iso_2_digit = 'CH'
    iso_3_digit = 'CHE'
    geometry = MultiPolygon(
        Polygon(((0, 0), (0, 1), (1, 1), (0, 0))),
        Polygon(((1, 1), (1, 2), (2, 2), (1, 1)))
    )

    class Meta:
        model = Country
