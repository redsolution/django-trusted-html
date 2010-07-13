from django.contrib import admin
from trustedhtml.grandma_setup.models import TrustedSettings, TrustedCutSite, TrustedObjectSite, TrustedModel, TrustedField

class TrustedCutSiteInline(admin.TabularInline):
    model = TrustedCutSite

class TrustedObjectSiteInline(admin.TabularInline):
    model = TrustedObjectSite

class TrustedForm(admin.ModelAdmin):
    model = TrustedSettings
    inlines = [TrustedCutSiteInline, TrustedObjectSiteInline]

class TrustedFieldInline(admin.TabularInline):
    model = TrustedField

class TrustedModelForm(admin.ModelAdmin):
    model = TrustedModel
    inlines = [TrustedFieldInline]

try:
    admin.site.register(TrustedSettings, TrustedForm)
except admin.sites.AlreadyRegistered:
    pass

try:
    admin.site.register(TrustedModel, TrustedModelForm)
except admin.sites.AlreadyRegistered:
    pass
