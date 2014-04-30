try:
    from django.conf.urls import patterns, url, include
except ImportError:
    from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
)

for view in ['response', 'notfound', 'error', 'redirect_response', 
    'redirect_notfound', 'redirect_redirect_response', 'redirect_cicle', 
    'permanent_redirect_response', 'http404', 'http500', 
    'request_true_response', 'request_false_response',]:
    urlpatterns += patterns('example.views', url('^%s$' % view, view, name=view))
