"""
Tables
http://www.w3.org/TR/1998/REC-CSS2-19980512/tables.html
"""

from trustedhtml.classes import List, Or, Sequence

from trustedhtml.rules.css.consts import inherit
from trustedhtml.rules.css.syndata import length

caption_side = List(values=[
    'top', 'bottom', 'left', 'right',
    'inherit',
])
# Applies to: 'table-caption' elements

table_layout = List(values=[
    'auto', 'fixed',
    'inherit',
])
# Applies to: 'table' and 'inline-table' elements

border_collapse = List(values=[
    'collapse', 'separate',
    'inherit',
])
# Applies to: 'table' and 'inline-table' elements

border_spacing_base = Sequence(rule=length, min_split=1, max_split=2)

border_spacing = Or(rules=[
    border_spacing_base, inherit,
])
# Applies to: 'table' and 'inline-table' elements
    
empty_cells = List(values=[
    'show', 'hide',
    'inherit',
])
# Applies to: 'table-cell' elements

speak_header = List(values=[
    'once', 'always',
    'inherit',
])
# Applies to: elements that have table header information  
