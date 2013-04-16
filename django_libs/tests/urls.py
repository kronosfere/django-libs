"""URLs to run the tests."""
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.http import HttpResponse

admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^index/', lambda x: HttpResponse('Success'), name='index'),
    url(r'^admin-.+/', include(admin.site.urls)),
)
