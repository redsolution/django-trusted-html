"""
The grammar of CSS2
http://www.w3.org/TR/1998/REC-CSS2-19980512/grammar.html

Specified rules not always corresponded to Syntax and basic data types
( http://www.w3.org/TR/1998/REC-CSS2-19980512/syndata.html )
So we custom it and add comments with source grammar.
"""

grammar = {}
grammar['h'] = r'([0-9a-f])' % grammar
grammar['w'] = r'([ \t\r\n\f]*)' % grammar
grammar['nl'] = r'(\n|\r\n|\r|\f)' % grammar
grammar['nonascii'] = r'([^\x00-\x7f])' % grammar
grammar['unicode'] = r'(\\%(h)s{1,6}[ \t\r\n\f]?)' % grammar
grammar['escape'] = r'(%(unicode)s|\\[ -~]|\\[^\x00-\x7f])' % grammar
grammar['nmstart'] = r'([a-z]|%(nonascii)s|%(escape)s)' % grammar
grammar['nmchar'] = r'([a-z0-9-]|%(nonascii)s|%(escape)s)' % grammar
grammar['string1'] = r'(\"(?P<string1>([\t !#$%%&(-~]|\\%(nl)s|\'|%(nonascii)s|%(escape)s)*)\")' % grammar
grammar['string2'] = r'(\'(?P<string2>([\t !#$%%&(-~]|\\%(nl)s|\"|%(nonascii)s|%(escape)s)*)\')' % grammar

grammar['ident'] = r'(%(nmstart)s%(nmchar)s*)' % grammar
# Not used:
#grammar['name'] = r'(%(nmchar)s+)' % grammar
grammar['string'] = r'(%(string1)s|%(string2)s)' % grammar
grammar['url'] = r'(?P<url>([!#$%%&*-~]|%(nonascii)s|%(escape)s)*)' % grammar
# Not used:
#grammar['range'] = r'(\?{1,6}|%(h)s(\?{0,5}|%(h)s(\?{0,4}|%(h)s(\?{0,3}|%(h)s(\?{0,2}|%(h)s(\??|%(h)s))))))' % grammar

# W3C grammar:
#grammar['num'] = r'([0-9]+|[0-9]*\.[0-9]+)' % grammar
grammar['int'] = r'([-+]?[0-9]+)' % grammar
grammar['real'] = r'([-+]?[0-9]*\.[0-9]+)' % grammar
grammar['num'] = r'(%(int)s|%(real)s)' % grammar

# W3C grammar:
#grammar['ems'] = r'(%(num)s(em))' % grammar
#grammar['exs'] = r'(%(num)s(ex))' % grammar
#grammar['length'] = r'(%(num)s(px|cm|mm|in|pt|pc))' % grammar
# Browsers support:
#grammar['length'] = r'(%(num)s(|px|cm|mm|in|pt|pc|em|ex))' % grammar
#W3C syntax and basic data types:
grammar['length'] = r'(%(num)s(px|cm|mm|in|pt|pc|em|ex)|0+)' % grammar
grammar['percentage'] = r'(%(num)s%%)' % grammar

grammar['positive-int'] = r'([0-9]+)' % grammar
grammar['positive-real'] = r'([0-9]*\.[0-9]+)' % grammar
grammar['positive-num'] = r'(%(positive-int)s|%(positive-real)s)' % grammar
grammar['positive-length'] = r'(%(positive-num)s(px|cm|mm|in|pt|pc|em|ex)|0+)' % grammar
grammar['positive-percentage'] = r'(%(positive-num)s%%)' % grammar
