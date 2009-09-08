"""
Visual effects
http://www.w3.org/TR/1998/REC-CSS2-19980512/visufx.html
"""

from trustedhtml.classes import List, RegExp, Or

from trustedhtml.rules.css.consts import auto, inherit
from trustedhtml.rules.css.grammar import grammar

overflow = List(values=[
    'visible', 'hidden', 'scroll', 'auto',
    'inherit',
])
# Applies to: block-level and replaced elements 

clip_shape = RegExp(
    regexp=r'(?P<n>rect)\('
        '%(w)s(?P<a>%(length)s|auto)%(w)s\,'
        '%(w)s(?P<b>%(length)s|auto)%(w)s\,'
        '%(w)s(?P<c>%(length)s|auto)%(w)s\,'
        '%(w)s(?P<d>%(length)s|auto)%(w)s\)$' % grammar,
    expand=r'\g<n>(\g<a>,\g<b>,\g<c>,\g<d>)',
)

clip = Or(rules=[
    clip_shape, auto, inherit,
])
# Applies to: block-level and replaced elements 

visibility = List(values=[
    'visible', 'hidden', 'collapse',
    'inherit',
])
