"""
``common`` dictionary contains common useful css rules.
``tables`` dictionary contains css rules for table`s elements.
``images`` dictionary contains css rules for element "img".
"""

from trustedhtml.utils import get_dict
from trustedhtml.classes import List, Or, Sequence
from trustedhtml.rules.css.consts import none, inherit
from trustedhtml.rules.css.values import values

disabled = [
    # It will break block formatting:
    'margin-top', 'margin-right', 'margin-bottom', 'margin-left',
    'margin',
    'padding-top', 'padding-right', 'padding-bottom', 'padding-left',
    'padding',
    # Maybe we need "display: inline;" to prevent breaking copy-pasted text?
    'display', # Fix: We must add processing: "display: none;"
    'position',
    'top', 'right', 'bottom', 'left',
    'z-index',
    'direction',
    'unicode-bidi',
    # It will break text formatting: 
    'line-height',
    # It isn`t useful
    # (IE not support it, and we don`t want to get different appearance)
    'min-width', 'min-height',
    'max-width', 'max-height',
    # It will break text formatting:
    'overflow',
    'clip',
    'visibility',
    # It will break list formatting:
    'content',
    'quotes',
    'counter-reset', 'counter-increment',
    'marker-offset',
    # Maybe we can enable list-styles for lists?
    'list-style-type',
    'list-style-image',
    'list-style-position',
    'list-style',
    # It will break printing (maybe we can enable it)?
    'size',
    'marks',
    'page-break-before', 'page-break-after',
    'page-break-inside',
    'page',
    'orphans', 'widows',
    # It will break color scheme:
    'color',
    # Maybe we can enable for tables?
    'background-color',
    'background-image',
    'background-repeat',
    'background-attachment',
    'background-position',
    'background',
    # It will break fonts:
    'font-family',
    'font-style',
    'font-variant',
    'font-weight',
    'font-stretch',
    'font-size',
    'font-size-adjust',
    'font',
    # It will break font settings:
    'text-indent',
    # It isn`t usable, so disable it:
    'text-shadow',
    # It will break font settings:
    'letter-spacing', 'word-spacing',
    # Maybe we can enable it ('capitalize', 'uppercase', 'lowercase', 'none',)?
    'text-transform',
    # Maybe it will be useful ('normal', 'pre', 'nowrap',)?
    'white-space',
    # It is not useful:
    'speak-header',
    # Maybe we need to set caption`s position for tables?
    # http://www.w3.org/TR/1998/REC-CSS2-19980512/tables.html#q6
    'caption-side',
    # It will break table`s building mechanism:
    'table-layout',
    # It will break table`s formatting (maybe enable it)?
    # http://www.w3.org/TR/1998/REC-CSS2-19980512/tables.html#borders
    'border-collapse',
    'border-spacing',
    'empty-cells',
    # It will break default cursors:
    'cursor',
    # It is not useful (use border instead):
    'outline-width',
    'outline-style',
    'outline-color',
    'outline',
]

for_table = [
    # We need borders for tables?
    'border-top-width', 'border-right-width', 'border-bottom-width', 'border-left-width',
    'border-width',
    'border-top-color', 'border-right-color', 'border-bottom-color', 'border-left-color',
    'border-color',
    'border-top-style', 'border-right-style', 'border-bottom-style', 'border-left-style',
    'border-style',
    'border-top', 'border-right', 'border-bottom', 'border-left', 'border',
    # We need vertical align:
    'vertical-align',
    # We need horizontal align:
    'text-align',
]

for_image = [
    # We need floating for images?
    'float',
]

for_table_and_image = [
    'width', 'height',
]

allowed = [
    # If we need float for image, we need it too:
    'clear',
    # We need it, but we must disable: 'blink'  
    'text-decoration',
]

text_decoration_base = List(values=[
    'underline', 'overline', 'line-through',
    # Disable: 'blink',
])

text_decoration = Or(rules=[
    Sequence(rule=text_decoration_base, min_split=1), none, inherit,
])

replace = {
    'text-decoration': text_decoration,
}

common = get_dict(source=values, leave=allowed, append=replace)
tables = get_dict(source=values, leave=allowed + for_table + for_table_and_image, append=replace)
images = get_dict(source=values, leave=allowed + for_image + for_table_and_image, append=replace)


#style_div = Style(rules={
#    'display': List(values=[
#        'none'], invalid=True),
#})
#
#style_span = Style(rules={
#    'text-decoration': List(values=[
#        'underline', 'line-through', 
#    ]),
#})
#
#style_td = Style(rules={
#    'border': border_complex,
#    'border-width': border_width,
#    'border-style': border_style,
#    'border-color': color,
#    
#    'margin': indent,
#    'padding': indent,
#
#    'margin-top': size,
#    'padding-top': size,
#
#    'width': size,
#    'height': size,
#
#    'white-space': List(values=[
#        'pre', 'nowrap', 'normal', 
#    ]),
#}, equivalents = {
#    'border': [
#        'border-top', 'border-bottom', 'border-left', 'border-right'
#    ],
#    'border-width': [
#        'border-top-width', 'border-bottom-width', 'border-left-width', 'border-right-width',
#    ],
#    'border-style': [
#        'border-top-style', 'border-bottom-style', 'border-left-style', 'border-right-style',
#    ],
#    'border-color': [
#        'border-top-color', 'border-bottom-color', 'border-left-color', 'border-right-color',
#    ],
#    'margin-top': [
#        'margin-bottom', 'margin-left', 'margin-right',
#    ],
#    'padding-top': [
#        'padding-bottom', 'padding-left', 'padding-right',
#    ],
#})
