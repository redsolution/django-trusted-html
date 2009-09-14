"""
Colors and Backgrounds
http://www.w3.org/TR/1998/REC-CSS2-19980512/colors.html
"""

from trustedhtml.classes import List, Or, Sequence, Complex

from trustedhtml.rules.css.consts import inherit, transparent, none
from trustedhtml.rules.css.syndata import length, percentage, color, uri_image

color = Or(rules=[
    color, inherit,
])

background_color = Or(rules=[
    color, transparent, inherit,  
])


background_image = Or(rules=[
    uri_image, none, inherit,
])


background_repeat = List(values=[
    'repeat', 'repeat-x', 'repeat-y', 'no-repeat',
    'inherit', 
])

background_attachment = List(values=[
    'scroll', 'fixed',
    'inherit', 
])

# W3C:
#background_position = Or(rules=[
#    Sequence(rule=
#        Or(rules=[
#            percentage, length,
#        ]),
#        min_split=1, max_split=2,
#    ),
#    Complex(rules=[
#        List(values=[
#            'left', 'center', 'right', 
#        ]),
#        List(values=[
#            'top', 'center', 'bottom',
#        ]),
#    ]),
#    inherit,
#])

background_position_x = Or(rules=[
    List(values=[
        'left', 'center', 'right', 
    ]),
    percentage,
    length,
])

background_position_y = Or(rules=[
    List(values=[
        'top', 'center', 'bottom',
    ]),
    percentage,
    length,
])

background_position = Or(rules=[
    Complex(rules=[
        background_position_x, 
        background_position_y,
    ]),
    inherit,
])


background = Or(rules=[
    Complex(rules=[
        background_color,
        background_image,
        background_repeat,
        background_attachment,
        background_position_x, 
        background_position_y,
    ]),
    inherit,
])
