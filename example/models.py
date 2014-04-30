from django.db import models
from trustedhtml.fields import TrustedTextField, TrustedCharField
from trustedhtml.rules.html import pretty


class MyModel(models.Model):
    html = TrustedTextField(validator=pretty)
    short = TrustedCharField(validator=pretty, max_length=100)


class ExternalModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    not_trusted = models.CharField(max_length=100)
