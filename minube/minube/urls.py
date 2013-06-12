from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'minube.views.home', name='home'),
    # url(r'^minube/', include('minube.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
