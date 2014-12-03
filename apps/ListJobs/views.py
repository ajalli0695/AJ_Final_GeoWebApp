from django.shortcuts import render
from django.views import generic
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.gis.geos import Point
from models import *
from forms import *


# Create your views here.


class MainView(generic.TemplateView):
    """Loads the main page"""
    template_name = 'ListJobs/main.html'


class MapView(generic.TemplateView):
    """Loads the main page"""
    template_name = 'ListJobs/Map.html'


def add_point(request):

    if request.method == 'POST':
        form = AddJobForm(request.POST)
        if form.is_valid():
            new_point = Jobs()
            cd = form.cleaned_data
            coordinates = cd['coordinates'].split(',')
            new_point.geom = Point(float(coordinates[0]), float(coordinates[1]))
            new_point.title = cd['title']
            new_point.address = cd['address']
            new_point.employer = cd['employer']

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
