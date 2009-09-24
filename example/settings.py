import os

DEBUG = False

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = 'trustedhtml.sqlite'
SITE_ID = 1

SECRET_KEY = 'x(qov*3gam=fi_o&wz1ndzz3g^e2qmplsa*6v8z6zmmzhf!ch8'

ROOT_URLCONF = 'example.urls'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'urlmethods',
    'trustedhtml',
    'example',
)
