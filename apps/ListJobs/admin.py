from django.contrib import admin

from apps.ListJobs import models


admin.site.register(models.Jobs)
admin.site.register(models.MapIt)


# Register your models here.