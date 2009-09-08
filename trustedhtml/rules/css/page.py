"""
Paged media
http://www.w3.org/TR/1998/REC-CSS2-19980512/page.html
"""

from trustedhtml.classes import List, Or, No

from trustedhtml.rules.css.consts import inherit, auto
from trustedhtml.rules.css.syndata import positive_integer, identifier

size = No()
# Applies to: the page context

marks = No()
# Applies to: the page context
 
page_break_before = List(values=[
    'auto', 'always', 'avoid', 'left', 'right',
    'inherit',
])
# Applies to: block-level elements 

page_break_inside = List(values=[
    'avoid', 'auto',
    'inherit',
])
# Applies to: block-level elements
 
page = Or(rules=[
    identifier, auto,
])
# Applies to: block-level elements

orphans = Or(rules=[
    positive_integer, inherit
])
# Applies to: block-level elements 
