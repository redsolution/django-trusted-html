# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

# Utility function to read the README file.  
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''

setup(
    name="redsolutioncms.django-trusted-html",
    version=__import__('trustedhtml').__version__,
    description=read('DESCRIPTION'),
    license="GPLv3",
    keywords="django html validation",

    author="Alexander Ivanov",
    author_email="alexander.ivanov@redsolution.ru",

    maintainer='Alexander Ivanov',
    maintainer_email='alexander.ivanov@redsolution.ru',

    url="https://github.com/redsolution/django-trusted-html",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Framework :: Django',
        'Environment :: Web Environment',
        'Natural Language :: Russian',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'Topic :: Internet :: WWW/HTTP :: Site Management :: Link Checking',
    ],
    packages=find_packages(exclude=['example', 'example.*']),
    install_requires=['django-url-methods>=0.2.0,<0.3'],
    include_package_data=True,
    zip_safe=False,
    long_description=read('README.rst'),
    entry_points={
        'redsolutioncms': ['trustedhtml = trustedhtml.redsolution_setup', ],
    }
)
