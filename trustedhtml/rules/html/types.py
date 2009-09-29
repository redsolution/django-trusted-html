"""
Basic HTML data types
http://www.w3.org/TR/REC-html40/types.html
"""

from trustedhtml.classes import String, RegExp, Uri, No, Sequence, Style

from trustedhtml.rules.html.grammar import grammar
from trustedhtml.rules import css

idref = name = RegExp(regexp=r'(%(name)s)$' % grammar)
name_required = RegExp(regexp=r'(%(name)s)$' % grammar, element_exception=True)

idrefs = RegExp(regexp=r'(%(name)s(%(w)s%(name)s)*)$' % grammar)
idrefs_comma = RegExp(regexp=r'(%(name)s(%(w)s,%(w)s%(name)s)*)$' % grammar)

number = RegExp(regexp=r'(%(number)s)$' % grammar)
number_required = RegExp(regexp=r'(%(number)s)$' % grammar, element_exception=True)
positive_number = RegExp(regexp=r'(%(positive-number)s)$' % grammar)


text = String()
text_required = String(element_exception=True)
text_default = String(default='')
uri = Uri()
uri_required = Uri(element_exception=True)
uri_image = Uri(type=Uri.IMAGE)
uri_image_required = Uri(type=Uri.IMAGE, element_exception=True)
uri_object = Uri(type=Uri.OBJECT)
uris = Sequence(rule=Uri())

color = RegExp(regexp=r'(%(color)s)$' % grammar)
# Browsers support more than 16 colors, so you can use color_list from css
# IE support rgb(r,g,b) format, so you can use color_list from css
#color = Or(rules=[
#    css.syndata.color_list,
#    css.syndata.color_spec,
#    RegExp(regexp=r'(#%(h)s{6})$' % grammar)
#])

pixels = RegExp(regexp=r'(%(number)s)$' % grammar)
length = RegExp(regexp=r'(%(length)s)$' % grammar)
multi_length = RegExp(regexp=r'(%(multi-length)s)$' % grammar)
multi_lengths = RegExp(regexp=r'(%(multi-length)s(%(w)s,%(w)s%(multi-length)s)*)$' % grammar)

length_required = RegExp(regexp=r'(%(length)s)$' % grammar, element_exception=True)

coords = RegExp(regexp=r'(%(length)s(%(w)s,%(w)s%(length)s)(%(w)s,%(w)s%(length)s)+)$' % grammar)

content_type = RegExp(regexp=r'(%(content-type)s)$' % grammar)
content_types = RegExp(regexp=r'(%(content-type)s(%(w)s,%(w)s%(content-type)s)*)$' % grammar)
content_type_required = RegExp(regexp=r'(%(content-type)s)$' % grammar, element_exception=True)

language_code = RegExp(regexp=r'(%(language-code)s)$' % grammar)

charset = RegExp(regexp=r'(%(charset)s)$' % grammar)
charsets = RegExp(regexp=r'(%(charset)s(%(w)s,?%(w)s%(charset)s)*)$' % grammar)

character = RegExp(regexp=r'(.)$')

datetime = RegExp(regexp=r'(%(datetime)s)$' % grammar)

link_types = RegExp(regexp=r'(%(link-types)s)$' % grammar)
# Full list (but "Authors may wish to define additional link types"):
# http://www.w3.org/TR/REC-html40/types.html#h-6.12

media_descs = Sequence(regexp=r'\s*,\s*', join_string=',', rule=
    RegExp(regexp=r'(%(media-desc)s)' % grammar), # Yes without $ in the end
)

style_sheet = css.full

frame_target = RegExp(regexp=r'(%(frame-target)s)$' % grammar)

script = No()
