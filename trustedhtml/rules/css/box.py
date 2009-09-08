"""
Box model
http://www.w3.org/TR/1998/REC-CSS2-19980512/box.html
"""

from trustedhtml.classes import List, Or, Sequence, Complex

from trustedhtml.rules.css.consts import inherit, auto, transparent
from trustedhtml.rules.css.syndata import length, percentage, positive_length, color

# Fast variant:
#    lexic['margin-width'] = '(%(length)s|%(percentage)s|auto)' % lexic
#    margin_top = RegExp(regexp=r'(%(margin-width)s|inherit)$' % lexic)
#    margin = Or(rules=[
#        Sequence(rule=RegExp(regexp=r'%(margin-width)s$' % lexic), min_split=1, max_split=4),
#        inherit,
#    ])

margin_width_base = Or(rules=[
    length, percentage, auto,
])

margin_top = Or(rules=[
    margin_width_base, inherit,
])

margin = Or(rules=[
    Sequence(rule=margin_width_base, min_split=1, max_split=4), inherit,
])


padding_width_base = Or(rules=[
    length, percentage,
])

padding_top = Or(rules=[
    padding_width_base, inherit,
])

padding = Or(rules=[
    Sequence(rule=padding_width_base, min_split=1, max_split=4), inherit,
])


border_width_base = Or(rules=[
    positive_length,
    List(values=[
        'thin', 'medium', 'thick',
    ])
])

border_top_width = Or(rules=[
    border_width_base, inherit,
])

border_width = Or(rules=[
    Sequence(rule=border_width_base, min_split=1, max_split=4), inherit,
])

border_top_color = Or(rules=[
    color, inherit,
])

border_color = Or(rules=[
    Sequence(rule=color, min_split=1, max_split=4), transparent, inherit,
])

border_style_base = List(values=[
    'none', 'hidden', 'dotted', 'dashed', 'solid', 'double', 
    'groove', 'ridge', 'inset', 'outset', 
])

border_top_style = Or(rules=[
    border_style_base, inherit,
])

border_style = Or(rules=[
    Sequence(rule=border_style_base, min_split=1, max_split=4), inherit,
])

border = Or(rules=[
    Complex(rules=[
        border_width_base,
        border_style_base,
        color,
    ]), inherit,
])
