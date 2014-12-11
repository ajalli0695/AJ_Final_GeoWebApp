from django.shortcuts import render
from django.views import generic
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.gis.geos import Point
from . import models
from . import forms


# Create your views here.

class SourcesView(generic.TemplateView):
    """Loads the sources page"""
    model = models.Jobs
    template_name = 'ListJobs/sources.html'


class MainView(generic.TemplateView):
    """Loads the main page"""
    template_name = 'ListJobs/main.html'


class MapView(generic.TemplateView):
    """Loads the main page"""
    template_name = 'ListJobs/Map.html'


class AddJobView(generic.CreateView):
    template_name = 'ListJobs/add_point.html'
    form_class = forms.AddJobForm
    model = models.Jobs
    success_url = '/add_point/success'


def add_point(request):

    if request.method == 'POST':
        form = AddJobForm(request.POST)
        if form.is_valid():
            new_point = Jobs()
            cd = form.cleaned_data
            coordinates = cd['coordinates'].split(',')
            new_point.geom = Point(float(coordinates[0]), float(coordinates[1]))
            new_point.title = cd['title']
            new_point.location = cd['location']
            new_point.employer = cd['employer']
            new_point.url = cd['url']
            new_point.save()
            return HttpResponseRedirect('/add_point/success')

        else:
            return HttpResponseRedirect('/add_point/error')
    else:
        form = AddJobForm()

    args = {}
    args.update(csrf(request))
    args['form'] = AddJobForm()

    return render_to_response('ListJobs/add_point.html', args)


def form_error(request):
    return render_to_response('ListJobs/form_error.html')


def form_success(request):
    return render_to_response('ListJobs/form_success.html')

