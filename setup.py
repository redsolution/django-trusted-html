# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

# Utility function to read the README file.  
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="redsolutioncms.django-trusted-html",
    version="0.1.0",
    description=("Django html and css validator" +
        " with GrandmaCMS integration"),
    license="LGPL",
    keywords="django html validation",

    author="Alexander Ivanov",
    author_email="alexander.ivanov@redsolution.ru",

    maintainer='Alexander Ivanov',
    maintainer_email='alexander.ivanov@redsolution.ru',

    url="http://packages.python.org/django-trusted-html",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: Freely Distributable',
        'Natural Language :: Russian',
        'Natural Language :: English',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'Topic :: Internet :: WWW/HTTP :: Site Management :: Link Checking',
    ],
    packages=find_packages(),
    install_requires=['django-url-methods==0.1.0'],
    include_package_data=True,
    zip_safe=False,
    long_description=open('README').read(),
    entry_points={
        'grandma_setup': ['trustedhtml = trustedhtml.grandma_setup', ],
    }
)
