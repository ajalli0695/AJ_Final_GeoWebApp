from __future__ import absolute_import
# import logging
from django.contrib.gis.db import models
# from django.contrib.auth.models import User
# from django.utils.translation import ugettext_lazy as _
# from django.conf import settings
# from geopy import geocoders
# from . import geocode


class Jobs(models.Model):
    """class for job listings"""
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    employer = models.CharField(max_length=50)
    url = models.URLField(max_length=200)
    geom = models.PointField(srid=4326)
    objects = models.GeoManager()

    def __str__(self):
        return "{}".format(self.title)


class Map(models.Model):
    """ class for mapping a particular job listing and it's employer's location """
    name = models.CharField(max_length=60)
    geom = models.PointField(srid=4326)
    objects = models.GeoManager()

    def __str__(self):
        return "{}".format(self.name)



# class Login(User.models):
#     """ class for creating user login to update job listings"""
