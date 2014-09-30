from django.conf.urls import patterns, include, url
from django.contrib import admin
# from apps. import json_views


extra_patterns=patterns('',

    url(r'^', include('apps.world.api_urls'), name='world'),
    url(r'^', include('apps.units.api_urls'), name='units'),

    )




urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'AJ_Final_GeoWebApp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
