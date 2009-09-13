"""
The grammar of HTML 4.0 based on
http://www.w3.org/TR/REC-html40/types.html
"""

grammar = {}
grammar['h'] = r'([0-9a-f])' % grammar
grammar['w'] = r'([ \t\r\n\f]*)' % grammar
grammar['name'] = r'([a-z][-_:.a-z0-9]*)' % grammar
grammar['number'] = r'([0-9]+)' % grammar
grammar['positive-number'] = r'([1-9][0-9]*)' % grammar
grammar['percentage'] = r'(%(number)s%%)' % grammar
grammar['length'] = r'(%(number)s|%(percentage)s)' % grammar
grammar['multi-length'] = r'(%(number)s|%(percentage)s|%(number)s\*|\*)' % grammar

grammar['color'] = r'(#%(h)s{6}|black|green|silver|lime|gray|olive|white|yellow|maroon|navy|red|blue|purple|teal|fuchsia|aqua)' % grammar

grammar['content-type'] = r'(text/html|image/(jpeg|png|gif)|audio/mpeg|video/mpeg|application/(x\-www\-form\-urlencoded|x\-shockwave\-flash)|multipart/form\-data)' % grammar
# Must be disabled: 'text/javascript', 'text/css', 
# Full list of types:
# http://www.iana.org/assignments/media-types/

grammar['language-code'] = r'([a-z]{1-8}(-[a-z]{1-8})*)' % grammar
# Specification:
# http://www.ietf.org/rfc/rfc1766.txt
# Full list of primary-tag (139 language codes):
# http://xml.coverpages.org/iso639a.html

grammar['charset'] = r'((?!utf-7$)([-+:.a-z0-9]+))' % grammar
# Disable 'utf-7' (because of possible XSS attacks)   
# Full list (828 charsets):
# http://www.iana.org/assignments/character-sets

grammar['datetime'] = r'([0-9]{4}-[0-1][0-9]-[0-3][0-9]T[0-2][0-9]:[0-5][0-9]:[0-5][0-9](Z|([-+][0-2][0-9]:[0-5][0-9])))' % grammar

grammar['link-types'] = r'(%(name)s(%(w)s%(name)s))' % grammar
# Full list (but "Authors may wish to define additional link types"):
# http://www.w3.org/TR/REC-html40/types.html#h-6.12

grammar['media-desc'] = r'([-a-z0-9]+)' % grammar
# Full list (but "Future versions of HTML may introduce new values"):
# http://www.w3.org/TR/REC-html40/types.html#h-6.12

grammar['frame-target'] = r'(_blank|_self|_parent|_top|[a-z]+)'
