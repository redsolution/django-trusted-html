"""
The grammar of HTML 4.0 based on
http://www.w3.org/TR/REC-html40/types.html
"""

grammar = {}
grammar['w'] = r'([ \t\r\n\f]*)' % grammar
grammar['name'] = r'([a-z][a-z0-9\-_:.]*)' % grammar
grammar['number'] = r'([0-9]+)' % grammar