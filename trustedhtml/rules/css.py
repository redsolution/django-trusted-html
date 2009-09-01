# -*- coding: utf-8 -*-

from trustedhtml.classes import *

# TODO: add it to Style
#core_css_values = [
#    'inherit',
#]

# TODO: CssUrl
css_url = Or(rules=[
    List(values=[
        'none'
    ]),
    Url(),
])

background_attachment = List(values=[
    'scroll', 'fixed',
])

background_color = Or(rules=[
    List(values=[
        'transparent', 
    ]),
    color, 
])

background_image = css_url

background_position_x = Or(rules=[
    size, 
    List(values=[
        'left', 'center', 'right', 
    ]),
])

background_position_y = Or(rules=[
    size, 
    List(values=[
        'top', 'center', 'bottom',
    ]),
])

background_position = Complex(trusted_sequence=[
    background_position_x,
    background_position_y,
])

background_repeat = List(values=[
    'repeat', 'repeat-x', 'repeat-y', 'no-repeat', 
])

background = Complex(trusted_sequence=[
    background_color,
    background_image,
    background_repeat,
    background_attachment,
    background_position,
])

border_color = Or(rules=[
    List(values=[
        'transparent', 
    ]),
    color, 
])


border_style = List(values=[
    'none', 'hidden', 'dotted', 'dashed', 'solid', 'double', 
    'groove', 'ridge', 'inset', 'outset', 
])

border_width = Or(rules=[
    size, 
    List(values=[
        'thin', 'medium', 'thick', 
    ]),
])

border_complex = Complex(trusted_sequence=[
    border_width,
    border_style,
    border_color,
])

border_collapse = List(values=[
    'collapse', 'separate',
])

border_spacing = Complex(trusted_sequence=[
    size,
    size,
])

bottom = Or(rules=[
    size, 
    List(values=[
        'auto',
    ]),
])

caption_side = List(values=[
    'top', 'bottom',
])

clear = List(values=[
    'left', 'right', 'both', 'none', 
])

clip = Or(rules=[
    List(values=[
        'auto', 
    ]),
    RegExp(regexp=
        '(rect\(%(w)s%(num)s%%?%(w)s\,%(w)s%(num)s%%?%(w)s\,%(w)s%(num)s%%?%(w)s\,%(w)s%(num)s%%?%(w)s\))$' % lexic_dict
    ),
])

cursor = List(values=[
    'auto', 'crosshair', 'default', 'e-resize', 'help', 'move', 'n-resize', 
    'ne-resize', 'nw-resize', 'pointer', 'progress', 's-resize', 'se-resize',
    'sw-resize', 'text', 'w-resize', 'wait',
])
# Don`t support URLs for cursor

direction = List(values=[
    'ltr', 'rtl',
])

display = List(values=[
    'none', 'block', 'inline', 'inline-block', 'inline-table', 'list-item',
    'run-in', 'table', 'table-caption', 'table-cell', 'table-column',
    'table-column-group', 'table-footer-group', 'table-header-group',
    'table-row', 'table-row-group',
])

empty_cells = List(values=[
    'hide', 'show', 
])

float = List(values=[
    'left', 'right', 
])

# TODO: font_family = Sequence(
#    RegExp(regexp=lexic_dict['string'])
#)
font_family = String()

font_size = Or(rules=[
    size, 
    List(values=[
        'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 
        'xx-large', 'smaller', 'larger',
    ]),
])

font_style = List(values=[
    'normal', 'italic', 'oblique',
])

font_variant = List(values=[
    'normal', 'small-caps',
])

font_weight = List(values=[
    'normal', 'bold', 'bolder', 'lighter',
    '100', '200', '300', '400', '500', '600', '700', '800', '900',
])

line_height = Or(rules=[
    size, 
    List(values=[
        'normal'
    ]),
])

font = Complex(trusted_sequence=[
    font_style,
    font_variant,
    font_weight,
    font_size,
    line_height,
    font_family,
    List(values=[
        'caption', 'icon', 'menu', 'message-box', 'small-caption', 'status-bar',
    ])
])

letter_spacing = Or(rules=[
    size, 
    List(values=[
        'normal'
    ]),
])

list_style_image = css_url

list_style_position = List(values=[
    'inside', 'outside'
])

list_style_type = List(values=[
    'none', 'circle', 'disc', 'square', 'armenian', 'decimal',
    'decimal-leading-zero', 'georgian', 'lower-alpha', 'lower-greek',
    'lower-latin', 'lower-roman', 'upper-alpha', 'upper-latin', 'upper-roman'
])

list_style = Complex(trusted_sequence=[
    list_style_type,
    list_style_position,
    list_style_image,
])

margin = Or(rules=[
    Indent(),
    List(values=[
        'auto'
    ]),
])

margin_top = Or(rules=[
    size, 
    List(values=[
        'auto'
    ]),
])

max_height = Or(rules=[
    size, 
    List(values=[
        'none'
    ]),
])

outline_color = Or(rules=[
    color,
    List(values=[
        'invert',
    ]),
])

outline_style = List(values=[
    'none', 'dotted', 'dashed', 'solid', 'double', 
    'groove', 'ridge', 'inset', 'outset', 
])

outline_width = border_width

outline_complex = Complex(trusted_sequence=[
    outline_color,
    outline_style,
    outline_width,
])

overflow = List(values=[
    'visible', 'hidden', 'scroll', 'auto',
])

page_break_after = List(values=[
    'auto', 'always', 'avoid', 'left', 'right',
])

page_break_inside = List(values=[
    'auto', 'avoid',
])

padding = Indent()

padding_top = Size()

position = List(values=[
    'absolute', 'fixed', 'relative', 'static',
])

quotes = Or(rules=[
    List(values=[
        'none',
    ]),
    RegExp(regexp=r'([%(w)s%(string)s[ \t\r\n\f]+%(string)s%(w)s]+)$'),
])

table_layout = List(values=[
    'auto', 'fixed',
])

text_align = List(values=[
    'left', 'right', 'center', 'justify', 
])

text_decoration = List(values=[
    'none', 'underline', 'overline', 'line-through', 'blink', 
])

text_indent = Size()

text_transform = List(values=[
    'none', 'capitalize', 'uppercase', 'lowercase', 
])

vertical_align = Or(rules=[
    size, 
    List(values=[
        'baseline', 'sub', 'super', 'top', 'text-top', 'middle', 'bottom', 
        'text-bottom',
    ]),
])

visibility = List(values=[
    'visible', 'hidden', 'collapse',
])

white_space = List(values=[
    'normal', 'nowrap', 'pre', 'pre-line', 'pre-wrap',
])

z_index = Or(rules=[
    List(values=[
        'auto',
    ]),
    number,
])

style = Style(trusted_list=[ {
    'background': background,
    'background-color': background_color,
    'background-image': background_image,
    'background-repeat': background_repeat,
    'background-attachment': background_attachment,
    'background-position': background_position,
    
    'border': border_complex,
    'border-width': border_width,
    'border-style': border_style,
    'border-color': color,
    'border-collapse': border_collapse,
    
    'bottom': bottom,
    'clear': clear,
    'color': color,
    
    # content is big security hole
    #'content':
    #'counter-increment': 
    #'counter-reset': 
    
    'margin': margin,
    'margin-top': margin_top,

    'padding': padding,
    'padding-top': padding_top,

    'width': size,
    'height': size,

    'float': float,
}, ], equivalents = {
    'border': [
        'border-top', 'border-bottom', 'border-left', 'border-right'
    ],
    'border-width': [
        'border-top-width', 'border-bottom-width', 'border-left-width', 'border-right-width',
    ],
    'border-style': [
        'border-top-style', 'border-bottom-style', 'border-left-style', 'border-right-style',
    ],
    'border-color': [
        'border-top-color', 'border-bottom-color', 'border-left-color', 'border-right-color',
    ],
    'bottom': [
        'height', 'left', 'right', 'top', 'width',
    ],
    'letter-spacing': [
        'word-spacing',
    ],
    'page-break-after': [
        'page-break-before',
    ],
    'margin-top': [
        'margin-bottom', 'margin-left', 'margin-right',
    ],
    'max-height': [
        'max-width',
    ],
    'padding-top': [
        'padding-bottom', 'padding-left', 'padding-right',
    ],
})
