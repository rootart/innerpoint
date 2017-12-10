from django.test import TestCase
from django.urls import reverse

from country.tests.factories import CountryFactory


class RandomCountryPointViewTestCase(TestCase):
    def setUp(self):
        self.country = CountryFactory()
        self.url = reverse('api-country-random-point', args=(self.country.iso_2_digit, ))

    def test_with_invalid_country_code(self):
        url = reverse('api-country-random-point', args=('pl', ))
        response = self.client.get(url)
        self.assertEqual(
            response.status_code,
            404
        )

    def test_with_valid_url(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

        response_json = response.json()

        required_data_keys = [
            'name', 'iso_2_digit', 'iso_3_digit', 'point',
        ]
        for key in required_data_keys:
            with self.subTest(key=key):
                self.assertIn(key, response_json)

        with self.subTest('check structure of the point'):
            point = response_json['point']
            self.assertIn('type', point)
            self.assertEqual(point['type'], 'Point')
            self.assertIn('coordinates', point)
