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
color_hex = RegExp(regexp=r'(#%(h)s{6})$' % grammar,)
color = Or(rules=[
    css.syndata.color_list,
    # Browsers support more than 16 colors, so use color_list from css
    css.syndata.color_spec,
    # IE support rgb(r,g,b) format, so use color_list from css
    color_hex,
])

