from rest_framework import serializers
from rest_framework_gis.fields import GeometryField


class RandomPointSerializer(serializers.Serializer):
    name = serializers.CharField()
    iso_2_digit = serializers.CharField()
    iso_3_digit = serializers.CharField()
    point = GeometryField(source='get_random_geometry_point')
