"""
User interface
http://www.w3.org/TR/1998/REC-CSS2-19980512/ui.html
"""

from trustedhtml.classes import List, Or, Sequence, Complex

from trustedhtml.rules.css.consts import inherit
from trustedhtml.rules.css.syndata import color, uri_image
from trustedhtml.rules.css.box import border_width_base, border_style_base

cursor_base = Or(rules=[
    List(values=[
        'auto', 'crosshair', 'default', 'pointer', 'move', 'e-resize', 'ne-resize',
        'nw-resize', 'n-resize', 'se-resize', 'sw-resize', 's-resize', 'w-resize',
        'text', 'wait', 'help'
    ]),
    uri_image,
])

cursor = Or(rules=[
    Sequence(rule=cursor_base, regexp=r'\s,\s', join_string=','),
    inherit,
])
# Bug: correct sequence is [<uri> ,]* list

outline_width = Or(rules=[
    border_width_base, inherit,
])

outline_style = Or(rules=[
    border_style_base, inherit,
])

outline_color_base = Or(rules=[
    color,
    List(values=[
        'invert',
    ]),
])

outline_color = Or(rules=[
    outline_color_base, inherit,
])

outline = Or(rules=[
    Complex(rules=[
        border_width_base,
        border_style_base,
        outline_color_base,
    ]), inherit,
])
