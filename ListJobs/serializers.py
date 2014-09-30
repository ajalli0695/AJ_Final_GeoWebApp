# from apps.units import models
from rest_framework import serializers
from rest_framework_gis import serializers as geoserializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Unit
        fields = ('id', 'name', 'status', 'desc')


class CountySerializer(geoserializers.GeoFeatureModelSerializer):
    class Meta:
        model = models.County
        geo_field = 'geom'
        fields = ('id', 'name')

