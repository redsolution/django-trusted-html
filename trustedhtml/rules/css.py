# -*- coding: utf-8 -*-

# W3C CSS2 Grammar ( http://www.w3.org/TR/1998/REC-CSS2-19980512/grammar.html )
# specified rules that not always corresponded to Syntax and basic data types section
# ( http://www.w3.org/TR/1998/REC-CSS2-19980512/syndata.html )
# So we will fix it and add comments with source grammar.

from trustedhtml.classes import RegExp, Sequence, Or, And, List, Url, Complex, String

lexic_dict = {}
lexic_dict['h'] = r'([0-9a-f])' % lexic_dict
lexic_dict['w'] = r'([ \t\r\n\f]*)' % lexic_dict
lexic_dict['nl'] = r'(\n|\r\n|\r|\f)' % lexic_dict
lexic_dict['nonascii'] = r'([^\x00-\x7f])' % lexic_dict
lexic_dict['unicode'] = r'(\\%(h)s{1,6}[ \t\r\n\f]?)' % lexic_dict
lexic_dict['escape'] = r'(%(unicode)s|\\[ -~]|\\[^\x00-\x7f])' % lexic_dict
lexic_dict['nmstart'] = r'([a-z]|%(nonascii)s|%(escape)s)' % lexic_dict
lexic_dict['nmchar'] = r'([a-z0-9-]|%(nonascii)s|%(escape)s)' % lexic_dict
lexic_dict['string1'] = r'(\"(?P<string1>([\t !#$%%&(-~]|\\%(nl)s|\'|%(nonascii)s|%(escape)s)*)\")' % lexic_dict
lexic_dict['string2'] = r'(\'(?P<string2>([\t !#$%%&(-~]|\\%(nl)s|\"|%(nonascii)s|%(escape)s)*)\')' % lexic_dict

lexic_dict['ident'] = r'(%(nmstart)s%(nmchar)s*)' % lexic_dict
lexic_dict['name'] = r'(%(nmchar)s+)' % lexic_dict

# W3C grammar:
#lexic_dict['num'] = r'([0-9]+|[0-9]*\.[0-9]+)' % lexic_dict
#W3C syntax and basic data types:
lexic_dict['int'] = r'([-+]?[0-9]+)' % lexic_dict
lexic_dict['real'] = r'([-+]?[0-9]*\.[0-9]+)' % lexic_dict
lexic_dict['num'] = r'(%(int)s|%(real)s)' % lexic_dict
lexic_dict['+int'] = r'([0-9]+)' % lexic_dict
lexic_dict['+real'] = r'([0-9]*\.[0-9]+)' % lexic_dict
lexic_dict['+num'] = r'(%(+int)s|%(+real)s)' % lexic_dict

lexic_dict['string'] = r'(%(string1)s|%(string2)s)' % lexic_dict
lexic_dict['url'] = r'(?P<url>([!#$%%&*-~]|%(nonascii)s|%(escape)s)*)' % lexic_dict
lexic_dict['range'] = r'(\?{1,6}|%(h)s(\?{0,5}|%(h)s(\?{0,4}|%(h)s(\?{0,3}|%(h)s(\?{0,2}|%(h)s(\??|%(h)s))))))' % lexic_dict

#W3C grammar:
#ems = RegExp(regexp='(%(num)s(em))$' % lexic_dict)
#exs = RegExp(regexp='(%(num)s(ex))$' % lexic_dict)
#length = RegExp(regexp='(%(num)s(px|cm|mm|in|pt|pc))$' % lexic_dict)
#W3C syntax and basic data types:
length = RegExp(regexp='((%(num)s(px|cm|mm|in|pt|pc|em|ex)|0+))$' % lexic_dict)
# Browsers:
#length = RegExp(regexp='(%(num)s(|px|cm|mm|in|pt|pc|em|ex))$' % lexic_dict)
  
angle = RegExp(regexp='(%(num)s(deg|rad|grad))$' % lexic_dict)
time = RegExp(regexp='(%(+num)s(ms|s))$' % lexic_dict)
freq = RegExp(regexp='(%(+num)s(hz|khz))$' % lexic_dict)
dimen = RegExp(regexp='(%(num)s%(ident)s)$' % lexic_dict)
percentage = RegExp(regexp='(%(num)s%%)$' % lexic_dict)
number = RegExp(regexp='(%(num)s)$' % lexic_dict)

size = RegExp(regexp=r'(%(num)s(|%%|px|cm|mm|in|pt|pc|em|ex))$' % lexic_dict)
indent = Sequence(rule=size, min_split=1, max_split=4)

color_spec = RegExp(
    regexp=r'(?P<n>rgb|hsl)\('
        '%(w)s(?P<a>%(int)s%%?)%(w)s\,'
        '%(w)s(?P<b>%(int)s%%?)%(w)s\,'
        '%(w)s(?P<c>%(int)s%%?)%(w)s\)$' % lexic_dict,
    expand=r'\g<n>(\g<a>,\g<b>,\g<c>)',
)
color_alpha = RegExp(
    regexp=r'(?P<n>rgba|hsla)\('
        '%(w)s(?P<a>%(int)s%%?)%(w)s\,'
        '%(w)s(?P<b>%(int)s%%?)%(w)s\,'
        '%(w)s(?P<c>%(int)s%%?)%(w)s\,'
        '%(w)s(?P<d>%(int)s%%?)%(w)s\)$' % lexic_dict,
    expand=r'\g<n>(\g<a>,\g<b>,\g<c>,\g<d>)',
)
color_hex = RegExp(regexp=r'(#%(h)s{3}|#%(h)s{6})$' % lexic_dict,)
color_list = List(values=[
    'activeborder', 'activecaption', 'appworkspace', 
    'background', 'buttonface', 'buttonhighlight', 'buttonshadow', 
    'buttontext', 'captiontext', 'graytext', 'highlight', 
    'highlighttext', 'inactiveborder', 'inactivecaption', 
    'inactivecaptiontext', 'infobackground', 'infotext', 'menu', 
    'menutext', 'scrollbar', 'threeddarkshadow', 'threedface', 
    'threedhighlight', 'threedlightshadow', 'threedshadow', 
    'window', 'windowframe', 'windowtext', 'currentcolor', 
] + [
    'aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure',  
    'beige', 'bisque', 'black', 'blanchedalmond', 'blue',
    'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse',
    'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson',
    'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray',
    'darkgreen', 'darkgrey', 'darkkhaki', 'darkmagenta',
    'darkolivegreen', 'darkorange', 'darkorchid', 'darkred',
    'darksalmon', 'darkseagreen', 'darkslateblue', 'darkslategray',
    'darkslategrey', 'darkturquoise', 'darkviolet', 'deeppink',
    'deepskyblue', 'dimgray', 'dimgrey', 'dodgerblue', 'firebrick',
    'floralwhite', 'forestgreen', 'fuchsia', 'gainsboro',
    'ghostwhite', 'gold', 'goldenrod', 'gray', 'green',
    'greenyellow', 'grey', 'honeydew', 'hotpink', 'indianred',
    'indigo', 'ivory', 'khaki', 'lavender', 'lavenderblush',
    'lawngreen', 'lemonchiffon', 'lightblue', 'lightcoral',
    'lightcyan', 'lightgoldenrodyellow', 'lightgray', 'lightgreen',
    'lightgrey', 'lightpink', 'lightsalmon', 'lightseagreen',
    'lightskyblue', 'lightslategray', 'lightslategrey',
    'lightsteelblue', 'lightyellow', 'lime', 'limegreen', 'linen',
    'magenta', 'maroon', 'mediumaquamarine', 'mediumblue',
    'mediumorchid', 'mediumpurple', 'mediumseagreen',
    'mediumslateblue', 'mediumspringgreen', 'mediumturquoise',
    'mediumvioletred', 'midnightblue', 'mintcream', 'mistyrose',
    'moccasin', 'navajowhite', 'navy', 'oldlace', 'olive',
    'olivedrab', 'orange', 'orangered', 'orchid', 'palegoldenrod',
    'palegreen', 'paleturquoise', 'palevioletred', 'papayawhip',
    'peachpuff', 'peru', 'pink', 'plum', 'powderblue', 'purple',
    'red', 'rosybrown', 'royalblue', 'saddlebrown', 'salmon',
    'sandybrown', 'seagreen', 'seashell', 'sienna', 'silver',
    'skyblue', 'slateblue', 'slategray', 'slategrey', 'snow',
    'springgreen', 'steelblue', 'tan', 'teal', 'thistle', 'tomato', 
    'turquoise', 'violet', 'wheat', 'white', 'whitesmoke',
    'yellow', 'yellowgreen', 
])

color = Or(rules=[
    color_list,
    color_spec,
    color_alpha,
    color_hex,
])

url = Or(rules=[
    And(rules=[
        RegExp(
            regexp=r'url\(%(w)s(%(string1)s)%(w)s\)' % lexic_dict,
            expand=r'\g<string1>',
        ),
        Url(),
        RegExp(regexp=r'(.*)$', expand='url(\"\\1\")', ),
    ]),
    And(rules=[
        RegExp(
            regexp=r'url\(%(w)s(%(string2)s)%(w)s\)' % lexic_dict,
            expand=r'\g<string2>',
        ),
        Url(),
        RegExp(regexp=r'(.*)$', expand='url(\'\\1\')', ),
    ]),
    And(rules=[
        RegExp(
            regexp=r'url\(%(w)s%(url)s%(w)s\)' % lexic_dict,
            expand=r'\g<url>',
        ),
        Url(),
        RegExp(regexp=r'(.*)$', expand='url(\\1)', ),
    ]),
])

inherit = List(values=[
    'inherit'
])

#

# TODO: add it to Style
#core_css_values = [
#    'inherit',
#]

background_attachment = List(values=[
    'scroll', 'fixed',
])

background_color = Or(rules=[
    List(values=[
        'transparent', 
    ]),
    color, 
])

background_image = Or(rules=[
    List(values=[
        'none'
    ]),
    url,
])

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

background_position = Complex(rules=[
    background_position_x,
    background_position_y,
])

background_repeat = List(values=[
    'repeat', 'repeat-x', 'repeat-y', 'no-repeat', 
])

background = Complex(rules=[
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

border = Complex(rules=[
    border_width,
    border_style,
    border_color,
])

border_collapse = List(values=[
    'collapse', 'separate',
])

border_spacing = Complex(rules=[
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
#    RegExp(regexp='(%(string)s)$' % lexic_dict)
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

font = Complex(rules=[
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

list_style_image = background_image

list_style_position = List(values=[
    'inside', 'outside'
])

list_style_type = List(values=[
    'none', 'circle', 'disc', 'square', 'armenian', 'decimal',
    'decimal-leading-zero', 'georgian', 'lower-alpha', 'lower-greek',
    'lower-latin', 'lower-roman', 'upper-alpha', 'upper-latin', 'upper-roman'
])

list_style = Complex(rules=[
    list_style_type,
    list_style_position,
    list_style_image,
])

margin = Or(rules=[
    indent,
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

outline_complex = Complex(rules=[
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

padding = indent

padding_top = size

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

text_indent = size

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
