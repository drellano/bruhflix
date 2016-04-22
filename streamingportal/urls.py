from django.conf.urls import url
from views import browse

urlpatterns = [
               url(r'^$', browse, name="streamingportal.browse"),
               ]
