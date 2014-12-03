from django import forms
from models import *


class AddJobForm(forms.Form):

    coordinates = forms.CharField(max_length=200, required=True)
    title = forms.CharField(max_length=40, required=True)
    address = forms.CharField(max_length=200, required=True)
    employer = forms.CharField(max_length=200, required=True)

    def clean(self):
        cleaned_data = self.cleaned_data

        coordinates = cleaned_data.get("coordinates")
        title = cleaned_data.get("title")
        address = cleaned_data.get("location")
        employer = cleaned_data.get("employer")

        return cleaned_data
