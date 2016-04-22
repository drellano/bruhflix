from django.conf.urls import include, url
from django.contrib import admin
from views import home

urlpatterns = [
               url(r'^$', home, name="home"),
               url(r'^browse/', include('streamingportal.urls')),
               url(r'^upload/', include('uploadconvert.urls')),

               url(r'^admin/', include(admin.site.urls)),
               ]
