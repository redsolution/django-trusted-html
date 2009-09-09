"""
Text
http://www.w3.org/TR/1998/REC-CSS2-19980512/text.html
"""

from trustedhtml.classes import List, Or, Sequence, Complex

from trustedhtml.rules.css.consts import inherit, normal, none
from trustedhtml.rules.css.syndata import length, percentage, string, color 

text_indent = Or(rules=[
    length, percentage, inherit,
])
# Applies to: block-level elements

text_align = Or(rules=[
    List(values=[
        'left', 'right', 'center', 'justify', 'inherit',
    ]),
    string,
])
# Applies to: block-level elements 

text_decoration_base = List(values=[
    'underline', 'overline', 'line-through', 'blink',
])

text_decoration = Or(rules=[
    Sequence(rule=text_decoration_base, min_split=1), none, inherit,
])

text_shadow_base = Complex(rules=[
    color,
    Sequence(rule=length, min_split=2, max_split=3),
], regexp=r'\s*,\s*', join_string=',', min_split=1)

text_shadow = Or(rules=[
    text_shadow_base, none, inherit,
])

letter_spacing = Or(rules=[
    length, normal, inherit,
])
 
text_transform = List(values=[
    'capitalize', 'uppercase', 'lowercase', 'none',
    'inherit',
])

white_space = List(values=[
    'normal', 'pre', 'nowrap',
    'inherit',
])
# Applies to: block-level elements 
