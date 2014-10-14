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
        fields = ['company_name', 'job_title', 'description', 'location']


class MapItFilter(django_filters.FilterSet):
    id = IntegerListFilter(name='id', lookup_type='in')

    class Meta:
        model = models.MapIt
        fields = ['name', 'geom']

class JobsCollection(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Jobs.objects.all()
    serializer_class = serializers.JobsSerializer
    filter_class = MarkerFilter


class MapItCollection(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.MapIt.objects.all()
    serializer_class = serializers.MapItSerializer
    filter_class = MapItFilter
