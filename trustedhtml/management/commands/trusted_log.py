# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from trustedhtml.models import Log
from trustedhtml.utils import get_lined

class Command(BaseCommand):
    help = '''Usage: manage.py trusted_log

Make files with source and result text of html validation.
For each record will be created two files:
    <id>s.txt - with source text,
    <id>r.txt - with result text.
'''

    def handle(self, *args, **options):
        if args:
            print self.help
            return
        lst = Log.objects.all()
        if not lst:
            print 'There is no elements in log.'
            return
        for obj in lst:
            print '%ds.txt' % obj.id,
            open('%ds.txt' % obj.id, 'w').write(get_lined(obj.source.encode('utf-8')))
            print '%dr.txt' % obj.id,
            open('%dr.txt' % obj.id, 'w').write(get_lined(obj.result.encode('utf-8')))
        print '\nDone.'
