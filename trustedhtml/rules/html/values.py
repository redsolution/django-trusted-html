# -*- coding: utf-8 -*-

from trustedhtml.classes import Style, List, Char, String, RegExp, Uri, Or
from trustedhtml.rules.css import index

title_a = String(default='', )

anchor = RegExp(regexp=r'^\s*(#\w+)$')

href = Or(rules=[
    Uri(required=True),
    anchor,
])

cite = Or(rules=[
    Uri(),
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

src = Uri(required=True, allow_sites=[])

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