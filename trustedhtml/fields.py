# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.admin.widgets import AdminTextareaWidget, AdminTextInputWidget

from trustedhtml.rules import pretty
from trustedhtml.widgets import TrustedTextarea, AdminTrustedTextarea, TrustedTextInput, AdminTrustedTextInput, TrustedTinyMCE, AdminTrustedTinyMCE

class TrustedTextField(models.TextField):
    """
    TextField with build-in validation.
    """
    def __init__(self, validator=pretty, *args, **kwargs):
        super(TrustedTextField, self).__init__(*args, **kwargs)
        self.validator = validator

    def formfield(self, **kwargs):
        defaults = {'widget': TrustedTextarea(validator=self.validator)}
        defaults.update(kwargs)

        if defaults['widget'] == AdminTextareaWidget:
            defaults['widget'] = AdminTrustedTextarea(validator=self.validator)

        return super(TrustedTextField, self).formfield(**defaults)

class TrustedCharField(models.CharField):
    """
    TextField with build-in validation.
    """
    def __init__(self, validator=pretty, *args, **kwargs):
        super(TrustedCharField, self).__init__(*args, **kwargs)
        self.validator = validator

    def formfield(self, **kwargs):
        defaults = {'widget': TrustedTextInput(validator=self.validator)}
        defaults.update(kwargs)

        if defaults['widget'] == AdminTextInputWidget:
            defaults['widget'] = AdminTrustedTextInput(validator=self.validator)

        return super(TrustedCharField, self).formfield(**defaults)

class TrustedHTMLField(models.TextField):
    """
    TextField with build-in validation.
    """
    def __init__(self, validator=pretty, *args, **kwargs):
        super(TrustedHTMLField, self).__init__(*args, **kwargs)
        self.validator = validator

    def formfield(self, **kwargs):
        defaults = {'widget': TrustedTinyMCE(validator=self.validator)}
        defaults.update(kwargs)

        if defaults['widget'] == AdminTextareaWidget:
            defaults['widget'] = AdminTrustedTinyMCE(validator=self.validator)

        return super(TrustedHTMLField, self).formfield(**defaults)
