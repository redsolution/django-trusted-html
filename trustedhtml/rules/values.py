# -*- coding: utf-8 -*-

from trustedhtml.classes import Style, List, Char, String, RegExp, Url, Or
from trustedhtml.rules import css

string = String()
number = RegExp(regexp=r'([-+]?\d{1,7})$')
length = RegExp(regexp=r'([-+]?\d{1,7}%?)$')
char = Char()

style = Style(rules={
    'background': css.background,
    'background-color': css.background_color,
    'background-image': css.background_image,
    'background-repeat': css.background_repeat,
    'background-attachment': css.background_attachment,
    'background-position': css.background_position,
    
    'border': css.border_complex,
    'border-width': css.border_width,
    'border-style': css.border_style,
    'border-color': css.color,
    'border-collapse': css.border_collapse,
    
    'bottom': css.bottom,
    'clear': css.clear,
    'color': css.color,
    
    # content is big security hole
    #'content':
    #'counter-increment': 
    #'counter-reset': 
    
    'margin': css.margin,
    'margin-top': css.margin_top,

    'padding': css.padding,
    'padding-top': css.padding_top,

    'width': css.size,
    'height': css.size,

    'float': css.float,
}, equivalents = {
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

link_type = List(values=[
    'alternate', 'stylesheet', 'start', 'next', 'prev', 
    'contents', 'index', 'glossary', 'copyright', 'chapter', 
    'section', 'subsection', 'appendix', 'help', 'bookmark',
] )

content_type = List(values=[
    'text/html', 'image/jpeg', 'image/png', 'image/gif', 'audio/mpeg', 'video/mpeg',    
    # Disabled: 'text/javascript', 'text/css', 
] ) # Full list: http://www.iana.org/assignments/media-types/

charset = List(values=[
    'utf-8', 'windows-1251', 'koi8-r', 'koi8-r', 'cp866', 'iso-8859-1', 'utf-16',
    # 'utf-7', # Disable (because of XSS)   
] ) # Full list: http://www.iana.org/assignments/character-sets

title_a = String(default='', )

anchor = RegExp(regexp=r'^\s*(#\w+)$')

href = Or(rules=[
    Url(required=True),
    anchor,
])

cite = Or(rules=[
    Url(),
    anchor,
])

clear = List(values=[
    'left', 'all', 'right', 'none', 
])

align = List(values=[
    'left', 'right', 'center', 'justify', 
])

align_caption = List(values=[
    'top', 'bottom', 'left', 'right', 
])

align_img = List(values=[
    'top', 'middle', 'bottom', 'left', 'right', 
])

align_table = List(values=[
    'left', 'center', 'right', 'justify', 'char', 
])

target = List(values=[
    '_blank', '_self', '_parent', '_top',
]),

name_a = String(required=True, )

src = Url(required=True, allow_sites=[])

alt = String(default='')

type_li = List(values=[
    'disc', 'square', 'circle', '1', 'a', 'A', 'i', 'I', 
])

type_ol = List(values=[
    '1', 'a', 'A', 'i', 'I', 
])

type_ul = List(values=[
    'disc', 'square', 'circle',
])

frame = List(values=[
    'void', 'above', 'below', 'hsides', 'lhs', 'rhs', 'vsides', 
    'box', 'border', 
])

rules = List(values=[
    'none', 'groups', 'rows', 'cols', 'all', 
])

valign = List(values=[
    'top', 'middle', 'bottom', 'baseline', 
])

scope = List(values=[
    'row', 'col', 'rowgroup', 'colgroup', 
])