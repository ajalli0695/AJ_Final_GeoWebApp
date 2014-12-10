from django.conf.urls import patterns, url

from apps.ListJobs import json_views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gisc2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^Jobs', json_views.JobsCollection.as_view(), name='Jobs'),
    #url(r'^Map', json_views.MapCollection.as_view(), name='Map'),
    )