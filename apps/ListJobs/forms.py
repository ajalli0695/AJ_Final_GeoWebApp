from django.contrib.gis import forms
from . import models


class AddJobForm(forms.ModelForm):

    class Meta:
        model = models.Jobs
        fields = ['title', 'location', 'employer', 'url', 'geom']

