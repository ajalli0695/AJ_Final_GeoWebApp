from rest_framework import serializers

from rest_framework_gis import serializers as geoserializers

from apps.ListJobs import models


class JobsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Jobs
        fields = ('id', 'title', 'location', 'employer', 'url')


class MapSerializer(geoserializers.GeoFeatureModelSerializer):
    class Meta:
        model = models.Map
        geo_field = 'geom'
        fields = ('id', 'name')

