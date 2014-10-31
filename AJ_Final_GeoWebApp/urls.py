from django.conf.urls import patterns, include, url
from django.contrib import admin


extra_patterns=patterns('',

    url(r'^', include('apps.ListJobs.api_urls'), name='Jobs'),
    )




urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'AJ_Final_GeoWebApp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('apps.ListJobs.urls', namespace='main')),
    (r'^accounts/', include('registration.backends.default.urls')),

)
