from django.test import TestCase

from country.models import Country
from django.contrib.gis.geos import Point
from .factories import CountryFactory


class TestCountryModel(TestCase):

    def test_get_random_geometry_point(self):
        country = CountryFactory()
        point = country.get_random_geometry_point()

        self.assertIsInstance(point, Point)

        with self.subTest('Point belongs to original geometry'):
            self.assertTrue(country.geometry.contains(point))

        with self.subTest('Check max num of SQL queries'):
            self.assertNumQueries(
                1,
                lambda: country.get_random_geometry_point()
            )

    def test_str_method(self):
        country = Country(name='Demo', iso_2_digit='de')
        self.assertEqual(country.__str__(), country.name)
