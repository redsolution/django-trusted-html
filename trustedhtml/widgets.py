from django.forms import Textarea
from django.forms import TextInput
from django.contrib.admin.widgets import AdminTextareaWidget

from trustedhtml.rules import pretty

class TrustedTextarea(Textarea):
    """
    Textarea with build-in validation.
    """

    def __init__(self, validator=pretty, *args, **kwargs):
        super(TrustedTextarea, self).__init__(*args, **kwargs)
        self.validator = validator

    def value_from_datadict(self, data, files, name):
        value = super(TrustedTextarea, self).value_from_datadict(data, files, name)
        return self.validator.validate(value)

class AdminTrustedTextarea(AdminTextareaWidget, TrustedTextarea):
    def __init__(self, validator=pretty, *args, **kwargs):
        super(AdminTrustedTextarea, self).__init__(*args, **kwargs)
        self.validator = validator

class TrustedTextInput(TextInput):
    """
    TextInput with build-in validation.
    """

    def __init__(self, validator=pretty, *args, **kwargs):
        super(TrustedTextInput, self).__init__(*args, **kwargs)
        self.validator = validator

    def value_from_datadict(self, data, files, name):
        value = super(TrustedTextInput, self).value_from_datadict(data, files, name)
        return self.validator.validate(value)

class AdminTrustedTextInput(AdminTextareaWidget, TrustedTextInput):
    def __init__(self, validator=pretty, *args, **kwargs):
        super(AdminTrustedTextInput, self).__init__(*args, **kwargs)
        self.validator = validator

try:
    from tinymce.widgets import TinyMCE
except ImportError:
    class TrustedTinyMCE(TrustedTextarea):
        pass

    class AdminTrustedTinyMCE(AdminTextareaWidget, TrustedTinyMCE):
        def __init__(self, validator=pretty, *args, **kwargs):
            super(AdminTrustedTinyMCE, self).__init__(*args, **kwargs)
            self.validator = validator

else:
    class TrustedTinyMCE(TinyMCE):
        """
        TinyMCE widget with build-in validation.
        """

        def __init__(self, validator=pretty, *args, **kwargs):
            super(TrustedTinyMCE, self).__init__(*args, **kwargs)
            self.validator = validator

        def value_from_datadict(self, data, files, name):
            value = super(TrustedTinyMCE, self).value_from_datadict(data, files, name)
            return self.validator.validate(value)

    class AdminTrustedTinyMCE(AdminTextareaWidget, TrustedTinyMCE):
        def __init__(self, validator=pretty, *args, **kwargs):
            super(AdminTrustedTinyMCE, self).__init__(*args, **kwargs)
            self.validator = validator

try:
    from pages.widgets_registry import register_widget
except ImportError:
    pass
else:
    register_widget(TrustedTextarea)
    register_widget(TrustedTextInput)
    register_widget(TrustedTinyMCE)
