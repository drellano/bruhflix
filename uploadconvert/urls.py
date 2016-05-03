from django.conf.urls import url, include
import views


urlpatterns = [
               url(r'^$', views.upload_file, name='upload'),
               url(r'^success/$', views.success, name='success'),
               url(r'^progressbarupload/', include('progressbarupload.urls')),
               ]
