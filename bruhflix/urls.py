from django.conf.urls import include, url
from django.contrib import admin
import views

urlpatterns = [
               url(r'^$', views.user_login, name="home"),
               url(r'^logout/$', views.user_logout, name="logout"),
               url(r'^browse/', include('streamingportal.urls')),
               url(r'^upload/', include('uploadconvert.urls')),
               url(r'^admin/', include(admin.site.urls)),
               ]
