# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from redsolutioncms.models import CMSSettings, BaseSettings

class TrustedSettingsManager(models.Manager):
    def get_settings(self):
        if self.get_query_set().count():
            return self.get_query_set()[0]
        else:
            trusted_settings = self.get_query_set().create()
            TrustedCutSite.objects.create(settings=trusted_settings, cut_site='127.0.0.1:8000')
            TrustedCutSite.objects.create(settings=trusted_settings, cut_site='localhost:8000')
            TrustedObjectSite.objects.create(settings=trusted_settings, object_site='youtube.com')
            TrustedObjectSite.objects.create(settings=trusted_settings, object_site='www.youtube.com')
            cms_settings = CMSSettings.objects.get_settings()
            if not cms_settings.package_was_installed('redsolutioncms.django-server-config'):
                TrustedCutSite.objects.create(settings=trusted_settings, cut_site='%s.com' % cms_settings.project_name)
                TrustedCutSite.objects.create(settings=trusted_settings, cut_site='www.%s.com' % cms_settings.project_name)
            return trusted_settings

class TrustedSettings(BaseSettings):
    objects = TrustedSettingsManager()

    enabled_log = models.BooleanField(verbose_name=_('Enable log'), blank=True)
    verify_sites = models.BooleanField(verbose_name=_('Verify sites'), blank=True)

class TrustedCutSite(models.Model):
    settings = models.ForeignKey(TrustedSettings, related_name='cut_sites')
    cut_site = models.CharField(verbose_name=_('Cut site'), max_length=255)

    def __unicode__(self):
        return self.cut_site

class TrustedObjectSite(models.Model):
    settings = models.ForeignKey(TrustedSettings, related_name='object_sites')
    object_site = models.CharField(verbose_name=_('Object site'), max_length=255)

    def __unicode__(self):
        return self.object_site

class TrustedModel(models.Model):
    settings = models.ForeignKey(TrustedSettings, related_name='models')
    model = models.CharField(verbose_name=_('Mode'), max_length=255)

class TrustedField(models.Model):
    model = models.ForeignKey(TrustedModel, related_name='fields')
    field = models.CharField(verbose_name=_('Field'), max_length=255)
