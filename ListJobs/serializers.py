from ListJobs import models
from rest_framework import serializers
from rest_framework_gis import serializers as geoserializers


class JobsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Jobs
        fields = ('company_name', 'job_title', 'description', 'location')


class MapItSerializer(geoserializers.GeoFeatureModelSerializer):
    class Meta:
        model = models.MapIt
        geo_field = 'geom'
        fields = ('name', 'geom')

