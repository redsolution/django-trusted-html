# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.admin.widgets import AdminTextareaWidget

from trustedhtml import pretty
from trustedhtml.widgets import TrustedWidget, AdminTrustedWidget

class TrustedField(models.TextField):
    """
    TextField with build-in validation.
    """
    def __init__(self, validator=pretty, *args, **kwargs):
        super(TrustedField, self).__init__(*args, **kwargs)
        self.validator = validator

    def formfield(self, **kwargs):
        defaults = {'widget': TrustedWidget(validator=self.validator)}
        defaults.update(kwargs)

        if defaults['widget'] == AdminTextareaWidget:
            defaults['widget'] = AdminTrustedWidget(validator=self.validator)

        return super(TrustedField, self).formfield(**defaults)
