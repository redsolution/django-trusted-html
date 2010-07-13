from grandma.make import BaseMake
from grandma.models import GrandmaSettings
from trustedhtml.grandma_setup.models import TrustedSettings

class Make(BaseMake):
    def make(self):
        super(Make, self).make()
        trustedhtml_settings = TrustedSettings.objects.get_settings()
        grandma_settings = GrandmaSettings.objects.get_settings()
        grandma_settings.render_to('settings.py', 'trustedhtml/grandma/settings.py', {
            'trustedhtml_settings': trustedhtml_settings,
        })
