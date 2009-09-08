"""
Visual formatting model details
http://www.w3.org/TR/1998/REC-CSS2-19980512/visudet.html
"""

from trustedhtml.classes import List, Or

from trustedhtml.rules.css.consts import inherit, normal, auto, none
from trustedhtml.rules.css.syndata import length, percentage, positive_number, positive_length, positive_percentage

width = Or(rules=[
    positive_length, positive_percentage, auto, inherit,
])
# Applies to: all elements but non-replaced inline elements, table rows, and row groups 

min_width = Or(rules=[
    positive_length, positive_percentage, inherit,
])
# Applies to: all elements except non-replaced inline elements and table elements 

max_width = Or(rules=[
    positive_length, positive_percentage, none, inherit,
])
# Applies to: all elements except non-replaced inline elements and table elements 

line_height = Or(rules=[
    normal, positive_number, positive_length, positive_percentage, inherit,
])

vertical_align = Or(rules=[
    List(values=[
        'baseline', 'sub', 'super', 'top', 'text-top', 'middle', 'bottom',
        'text-bottom',
    ]), length, percentage, inherit,
])
# Applies to: inline-level and 'table-cell' elements
