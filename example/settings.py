import os

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'trustedhtml.sqlite',
    }
}
SITE_ID = 1

SECRET_KEY = 'x(qov*3gam=fi_o&wz1ndzz3g^e2qmplsa*6v8z6zmmzhf!ch8'

ROOT_URLCONF = 'example.urls'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'urlmethods',
    'trustedhtml',
    'example',
)

TRUSTEDHTML_OBJECT_SITES = [
    'youtube.com',
    'www.youtube.com',
]

MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'static')
STATIC_URL = '/static/'

TRUSTEDHTML_MODELS = [
    {
        'model': 'example.models.ExternalModel',
        'fields': ['description', 'name', ],
    },
]
