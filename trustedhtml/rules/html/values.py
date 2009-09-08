# -*- coding: utf-8 -*-

from trustedhtml.classes import Style, List, Char, String, RegExp, Url, Or
from trustedhtml.rules.css import index

string = String()
number = RegExp(regexp=r'([-+]?\d{1,7})$')
length = RegExp(regexp=r'([-+]?\d{1,7}%?)$')
char = Char()

style = Style(rules=index)

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