from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', view='browse', name='streamingportal.browse'),
)
