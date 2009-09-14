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
    # It will break view:
    'border-top-width', 'border-right-width', 'border-bottom-width', 'border-left-width',
    'border-width',
    'border-top-color', 'border-right-color', 'border-bottom-color', 'border-left-color',
    'border-color',
    'border-top-style', 'border-right-style', 'border-bottom-style', 'border-left-style',
    'border-style',
    'border-top', 'border-right', 'border-bottom', 'border-left', 'border',
    # It will break block formatting:
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
    'list-style-type',
    'list-style-image',
    'list-style-position',
    'list-style',
    # It will break printing:
    'size',
    'marks',
    'page-break-before', 'page-break-after',
    'page-break-inside',
    'page',
    'orphans', 'widows',
    # It will break color scheme:
    'color',
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
    'text-transform',
    'white-space',
    # It is not useful:
    'speak-header',
    # It will break table`s view:
    'caption-side',
    # It will break table`s building mechanism:
    'table-layout',
    # It will break table`s formatting:
    # http://www.w3.org/TR/1998/REC-CSS2-19980512/tables.html#borders
    'border-collapse',
    'border-spacing',
    'empty-cells',
    # It will break default cursors:
    'cursor',
    # It will break block formatting:
    'outline-width',
    'outline-style',
    'outline-color',
    'outline',
]

for_table = [
    # We need vertical align:
    # (for other elements it will break text formatting)
    'vertical-align',
    # We need horizontal align:
    # (for other elements it will break text formatting)
    'text-align',
]

for_image = [
    # We need floating for images:
    # (for other elements it will break block formatting)
    'float',
    # We need size of images.
    # (for other elements it will break block formatting)
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
tables = get_dict(source=values, leave=allowed + for_table, append=replace)
images = get_dict(source=values, leave=allowed + for_image, append=replace)

#style_div = Style(rules={
#    'display': List(values=[
#        'none'], invalid=True, element_exception=True),
#})
