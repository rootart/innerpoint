from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import RandomPointSerializer
from .models import Country

class RandomCountryPointView(APIView):

    def get_serializer(self, country):
        return RandomPointSerializer(country)

    def get(self, request, *args, **kwargs):
        iso_2_digit = kwargs.get('iso_2_digit').upper()
        country = Country.objects.get(iso_2_digit=iso_2_digit)
        serializer = self.get_serializer(country)
        return Response(serializer.data)
