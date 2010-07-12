try:
    from tinymce.widgets import TinyMCE as Textarea
except ImportError:
    from django.forms import Textarea
from django.contrib.admin.widgets import AdminTextareaWidget

from trustedhtml import pretty

class TrustedWidget(Textarea):
    """
    Textarea with build-in validation.
    TinyMCE widget will be used if possible.
    """

    def __init__(self, validator=pretty, *args, **kwargs):
        super(TrustedWidget, self).__init__(*args, **kwargs)
        self.validator = validator

    def value_from_datadict(self, data, files, name):
        value = super(TrustedWidget, self).value_from_datadict(data, files, name)
        return self.validator.validate(value)

class AdminTrustedWidget(AdminTextareaWidget, TrustedWidget):
    pass

try:
    from pages.widgets_registry import register_widget
except ImportError:
    pass
else:
    register_widget(TrustedWidget)
