from django.conf import settings

TRUSTEDHTML_ENABLE_LOG = getattr(settings, 'TRUSTEDHTML_ENABLE_LOG', False)

TRUSTEDHTML_LINK_SITES = getattr(settings, 'TRUSTEDHTML_LINK_SITES', True)
TRUSTEDHTML_IMAGE_SITES = getattr(settings, 'TRUSTEDHTML_IMAGE_SITES', True)
TRUSTEDHTML_OBJECT_SITES = getattr(settings, 'TRUSTEDHTML_OBJECT_SITES', True)

TRUSTEDHTML_ALLOW_SCHEMES = getattr(settings, 'TRUSTEDHTML_ALLOW_SCHEMES', [
    'http', 'https', 'shttp', 'ftp', 'sftp', 'file', 'mailto',
    'svn', 'svn+ssh', 'telnet', 'mms', 'ed2k', ])

TRUSTEDHTML_CUT_SITES = getattr(settings, 'TRUSTEDHTML_CUT_SITES', False)
TRUSTEDHTML_CUT_SCHEMES = getattr(settings, 'TRUSTEDHTML_CUT_SCHEMES', [
    'http', ])

TRUSTEDHTML_VERIFY_SITES = getattr(settings, 'TRUSTEDHTML_VERIFY_SITES', False)
TRUSTEDHTML_VERIFY_SCHEMES = getattr(settings, 'TRUSTEDHTML_VERIFY_SCHEMES', [
    'http', 'https', 'ftp', ],)

TRUSTEDHTML_VERIFY_LOCAL = getattr(settings, 'TRUSTEDHTML_VERIFY_LOCAL', False)

TRUSTEDHTML_LOCAL_SITES = getattr(settings, 'TRUSTEDHTML_LOCAL_SITES', False)
TRUSTEDHTML_LOCAL_SCHEMES = getattr(settings, 'TRUSTEDHTML_LOCAL_SCHEMES', [
    'http', ],)

TRUSTEDHTML_MODELS = getattr(settings, 'TRUSTEDHTML_MODELS', [])

TRUSTEDHTML_USE_MODELURL = getattr(settings, 'TRUSTEDHTML_USE_MODELURL', 'modelurl' in settings.INSTALLED_APPS)
