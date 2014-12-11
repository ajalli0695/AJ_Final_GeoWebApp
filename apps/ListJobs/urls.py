from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from apps.ListJobs import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gisc2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^main$', views.MainView.as_view()),
    url(r'^Map$', views.MapView.as_view()),
    url(r'^$', login_required(views.MainView.as_view())),
    url(r'^add_point/$', views.AddJobView.as_view(), name='add_job'),
    url(r'^add_point/error$', 'apps.ListJobs.views.form_error'),
    url(r'^add_point/success$', 'apps.ListJobs.views.form_success'),
    url(r'^sources$', views.SourcesView.as_view()),
)
