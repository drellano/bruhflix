from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'bruhflix.views.home', name='home'),
    url(r'^browse/', include('streamingportal.urls')),
    url(r'^upload/', include('uploadconvert.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
