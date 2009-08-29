# -*- coding: utf-8 -*-

import urllib2

from django.core.files import File

class UrlFile(File):
    def __init__(self, url, max_length=None):
        self.max_length = max_length
        self.url = url
        
        # Do it to repeat initialization (for reopening)
        if hasattr(self, '_size'):
            delattr(self, '_size')
        
        response = urllib2.urlopen(urllib2.Request(
            self.url, None, 
            { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' }))

        # Do it instead of super(UrlFile, self).__init__(response.fp)
        self.file = response.fp
        
        # Fix for work with FTP
        if hasattr(self.file, 'name'):
            self._name = self.file.name
        else:
            self._name = ''
        if hasattr(self.file, 'mode'):
            self._mode = self.file.mode
        else:
            self._mode = 'rb'
        self._closed = False

        # Get file size
        self.fixed_size = True
        if not hasattr(self.file, 'size'):
            # ... from HTTP
            size = None
            headers = response.info()
            if 'Content-Length' in headers:
                try:
                    size = int(headers['Content-Length'])
                except (ValueError, OverflowError):
                    pass
            if size is not None:
                self.size = size
            else:
                # Unknown file size, we get it while read operation
                self.fixed_size = False
                self.size = 0
        try:
            if self.max_length is not None and self.size > self.max_length:
                raise ValueError('Too much size')
        except AttributeError:
            pass

    def chunks(self, chunk_size=None):
        if not chunk_size:
            chunk_size = self.__class__.DEFAULT_CHUNK_SIZE
        if hasattr(self.file, 'seek'):
            # Seek if we can
            self.seek(0)
        else:
            # Reopen if we can`t
            # TODO: move __init__ to normal function
            self.__init__(self.url)
        if self.fixed_size:
            left = self.size
        else:
            left = 1
        while left > 0:
            data = self.read(chunk_size)
            yield data
            if self.fixed_size:
                left -= chunk_size
            else:
                # Break reading for unknown size only when no data received
                if not data:
                    break
            
    def read(self, num_bytes=None):
        if num_bytes is None:
            data = self.file.read()
        else:
            data = self.file.read(num_bytes)
        if not self.fixed_size:
            self.size += len(data)
        return data
