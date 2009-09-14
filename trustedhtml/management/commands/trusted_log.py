# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from trustedhtml.models import Log
from trustedhtml.utils import get_lined

class Command(BaseCommand):
    help = '''Usage: manage.py trusted_log [source-file-name] [result-file-name]

Make files with source and result text of html validation.

source-file-name -  is template to generate file name for source text
                    by default: '%ds.txt'
result-file-name - is template to generate file name for source text
                    by default: '%dr.txt'
'''

    def handle(self, *args, **options):
        if len(args) > 2:
            print self.help
            return
        try:
            source = args[0]
        except IndexError:
            source = '%06ds.txt'
        try:
            result = args[1]
        except IndexError:
            result = '%06dr.txt'
        lst = Log.objects.all()
        if not lst:
            print 'There is no elements in log.'
            return
        for obj in lst:
            print source % obj.id,
            open(source % obj.id, 'w').write(get_lined(obj.source.encode('utf-8')))
            print result % obj.id,
            open(result % obj.id, 'w').write(get_lined(obj.result.encode('utf-8')))
        print '\nDone.'
