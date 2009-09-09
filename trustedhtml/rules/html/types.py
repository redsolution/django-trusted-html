"""
Basic HTML data types
http://www.w3.org/TR/REC-html40/types.html
"""

from trustedhtml.rules.html.grammar import grammar
from trustedhtml.rules import css

from trustedhtml.classes import String, RegExp, Uri

cdata = String()
idref = name = id = RegExp(regexp=r'(%(name)s)$' % grammar)
idrefs = RegExp(regexp=r'(%(name)s(%(w)s%(name)s)*)$' % grammar)
number = RegExp(regexp=r'(%(number)s)$' % grammar)
text = String()
uri = Uri()
uri_required = Uri(required=True)

color = RegExp(regexp=r'(%(color)s)$' % grammar)
# Browsers support more than 16 colors, so you can use color_list from css
# IE support rgb(r,g,b) format, so you can use color_list from css
#color = Or(rules=[
#    css.syndata.color_list,
#    css.syndata.color_spec,
#    RegExp(regexp=r'(#%(h)s{6})$' % grammar)
#])

pixels = RegExp(regexp=r'(%(int)s)$' % grammar)
length = RegExp(regexp=r'(%(int)s|%(percentage)s)$' % grammar)
multi_length = RegExp(regexp=r'(%(int)s|%(percentage)s|%(int)s\*|\*)$' % grammar)

content_type = RegExp(regexp=r'(%(content-type)s)$' % grammar)
content_types = RegExp(regexp=r'(%(content-type)s(%(w)s,%(w)s%(content-type)s)$' % grammar)

language_code = RegExp(regexp=r'(%(language-code)s)$' % grammar)

charset = RegExp(regexp=r'(%(charset)s)$' % grammar)
charsets = RegExp(regexp=r'(%(charset)s(%(w)s,?%(w)s%(charset)s)*)$' % grammar)

character = RegExp(regexp=r'(.)$')

datetime = RegExp(regexp=r'(%(datetime)s)$' % grammar)

link_types = RegExp(regexp=r'(%(link-types)s)$' % grammar)
# Full list (but "Authors may wish to define additional link types"):
# http://www.w3.org/TR/REC-html40/types.html#h-6.12

media_desc = Sequence(regexp=r'\s*,\s*', join_string=',', rule=
    RegExp(regexp=r'(%(media-desc)s)' % grammar), # Yes without $ in the end
)

style_sheet = Style(rules=css.index, 
#    allowed_value=List(values='inherit'),
)

frame_target = RegExp(regexp=r'(%(frame-target)s)$' % grammar)
