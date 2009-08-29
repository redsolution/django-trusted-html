# -*- coding: utf-8 -*-

import urllib2

import os
import urlparse

from files.file import UrlFile
from django.db import IntegrityError

class TrustedHandler(object):
    def __init__(self, profile):
        self.profile = profile
        
    def listener(self, rule, value, state):
        if state == 'local_only' and rule.tag == 'download_image':
            from publication.models import Image
            uploaded = Image.objects.filter(profile=self.profile, name=value).order_by('-created')
            if uploaded.count():
                return uploaded[:1][0].image.url
            try:
                file = UrlFile(value)
            except IOError, error:
                return None
            except OSError, error:
                return None
            instance = Image(profile=self.profile, name=value)
            path = urlparse.urlparse(value)[2]
            name = os.path.basename(path)
            if not name:
                path = os.path.split(path)[0]
                name = os.path.basename(path)
            if not name:
                name = 'upload'
            try:
                instance.image.save(name, file)
            except (IntegrityError, ValueError), error:
                return None
            return instance.image.url
        return None
        
