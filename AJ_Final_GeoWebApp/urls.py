from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required


api_patterns = patterns('',
    url(r'^', include('apps.ListJobs.api_urls'), name='Jobs'),
)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'AJ_Final_GeoWebApp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api/v1/', include(api_patterns, namespace='api')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('apps.ListJobs.urls', namespace='main')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    # url(r'^Map/', include('apps.ListJobs.urls', namespace='Map')),


)
