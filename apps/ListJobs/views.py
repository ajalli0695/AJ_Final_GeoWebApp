from django.shortcuts import render
from django.views import generic

# Create your views here.


class MainView(generic.TemplateView):
    """Loads the main page"""
    template_name = 'main.html'


class NextView(generic.TemplateView):
    """Loads the main page"""
    template_name = 'next.html'

