from django.conf.urls import url
from views import upload

urlpatterns = [
               url(r'^$', upload, 'uploadconver.upload'),
               ]
