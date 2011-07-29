from redsolutioncms.make import BaseMake
from redsolutioncms.models import CMSSettings
from trustedhtml.redsolution_setup.models import TrustedSettings

class Make(BaseMake):
    def postmake(self):
        super(Make, self).postmake()
        trustedhtml_settings = TrustedSettings.objects.get_settings()
        cms_settings = CMSSettings.objects.get_settings()
        cms_settings.render_to('settings.py', 'trustedhtml/redsolutioncms/settings.pyt', {
            'trustedhtml_settings': trustedhtml_settings,
            'server_config_was_installed': cms_settings.package_was_installed('redsolutioncms.django-server-config'),
         })

make = Make()
