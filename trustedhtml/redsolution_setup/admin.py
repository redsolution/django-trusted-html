from django.contrib import admin
from trustedhtml.redsolution_setup.models import TrustedSettings, TrustedCutSite, TrustedObjectSite, TrustedModel, TrustedField
from redsolutioncms.admin import CMSBaseAdmin

class TrustedCutSiteInline(admin.TabularInline):
    model = TrustedCutSite

class TrustedObjectSiteInline(admin.TabularInline):
    model = TrustedObjectSite

class TrustedSettingsAdmin(CMSBaseAdmin):
    model = TrustedSettings
    inlines = [TrustedCutSiteInline, TrustedObjectSiteInline]

# Native django admin for debug
class TrustedNativeAdmin(admin.ModelAdmin):
    model = TrustedSettings
    inlines = [TrustedCutSiteInline, TrustedObjectSiteInline]

class TrustedFieldInline(admin.TabularInline):
    model = TrustedField

class TrustedModelForm(admin.ModelAdmin):
    model = TrustedModel
    inlines = [TrustedFieldInline]

try:
    admin.site.register(TrustedSettings, TrustedNativeAdmin)
except admin.sites.AlreadyRegistered:
    pass

try:
    admin.site.register(TrustedModel, TrustedModelForm)
except admin.sites.AlreadyRegistered:
    pass
