from django.contrib.gis import admin
from apps.ListJobs import models


admin.site.register(models.Map)
admin.site.register(models.Jobs, admin.OSMGeoAdmin)

# Register your models here.