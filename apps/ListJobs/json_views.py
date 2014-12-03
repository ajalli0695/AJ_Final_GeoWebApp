from rest_framework import generics
import django_filters

from apps.ListJobs import serializers
from apps.ListJobs import models


class IntegerListFilter(django_filters.Filter):
    def filter(self, qs, value):
        if value not in (None, ''):
            integers = [int(v) for v in value.split(',')]
            return qs.filter(**{'{}__{}'.format(self.name, self.lookup_type): integers})
        return qs


class MarkerFilter(django_filters.FilterSet):
    id = IntegerListFilter(name='id', lookup_type='in')

    class Meta:
        model = models.Jobs
        fields = ['id', 'title', 'location', 'employer', 'url']


class MapFilter(django_filters.FilterSet):
    id = IntegerListFilter(name='id', lookup_type='in')

    class Meta:
        model = models.Map
        geo_field = 'geom'
        fields = ['id', 'name']


class JobsCollection(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Jobs.objects.all()
    serializer_class = serializers.JobsSerializer
    filter_class = MarkerFilter


class MapCollection(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Map.objects.all()
    serializer_class = serializers.MapSerializer
    filter_class = MapFilter
