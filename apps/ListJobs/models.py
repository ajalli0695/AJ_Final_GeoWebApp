from django.contrib.gis.db import models


class Jobs(models.Model):
    """class for job listings"""
    company_name = models.CharField(max_length=40)
    job_title = models.CharField(max_length=280)
    description = models.CharField(max_length=280)
    location = models.CharField(max_length=280)

    def __str__(self):
        return "{}".format(self.name)


class MapIt(models.Model):
    """ class for mapping a particular job """
    name = models.CharField(max_length=60)
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()

    def __str__(self):
        return "{}".format(self.name)

