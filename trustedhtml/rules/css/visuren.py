"""
Visual formatting model
http://www.w3.org/TR/1998/REC-CSS2-19980512/visuren.html
"""

from trustedhtml.classes import List, Or

from trustedhtml.rules.css.consts import inherit, auto
from trustedhtml.rules.css.syndata import length, percentage, integer

display = List(values=[
    'inline', 'block', 'list-item', 'run-in', 'compact', 'marker', 'table',
    'inline-table', 'table-row-group', 'table-header-group',
    'table-footer-group', 'table-row', 'table-column-group',
    'table-column', 'table-cell', 'table-caption', 'none',
    'inherit'
])

position = List(values=[
    'static', 'relative', 'absolute', 'fixed',
    'inherit',
])

top = Or(rules=[
    length, percentage, auto, inherit
])
# Applies to: positioned elements 

float = List(values=[
    'left', 'right', 'none',
    'inherit', 
])

clear = List(values=[
    'none', 'left', 'right', 'both',
    'inherit', 
])
# Applies to: block-level elements 

z_index = Or(rules=[
    auto, integer, inherit
])
# Applies to: positioned elements  

direction = List(values=[
    'ltr', 'rtl',
    'inherit',
])

unicode_bidi = List(values=[
    'normal', 'embed', 'bidi-override',
    'inherit',
])
