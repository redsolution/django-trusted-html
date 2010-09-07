# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url
from trustedhtml.redsolution_setup.admin import TrustedSettingsAdmin

admin_instance = TrustedSettingsAdmin()

urlpatterns = patterns('',
    url(r'^$', admin_instance.change_view, name='trustedhtml_index'),
)
