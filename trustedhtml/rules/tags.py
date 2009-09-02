# -*- coding: utf-8 -*-

from trustedhtml.classes import *
from trustedhtml.rules.common import *
from trustedhtml.rules import attributes

a = Or(allow_empty=True, rules=[
    Attributes(rules={
        'title': String(default=''),
        # Can enable: 'charset': attributes.charset,
        # Can enable: 'type': attributes.content_type,
        'name': string,
        'href': Url(allow_anchor=True, required=True), 
        # Can enable: 'rel': attributes.link_type,    or     string,
        # Can enable: 'rev': attributes.link_type,    or     string,
        # Can enable: 'accesskey': char,
        # Can enable: 'shape':  List(values=['rect', 'circle', 'poly', 'default', ] ),
        # Can enable: 'coords': Sequence(validator=number, delimiter_regexp='\s*,\s*'),
        # Can enable: 'tabindex': number,
        'target': List(values=['_blank', '_self', '_parent', '_top', ]), 
    }),
    Attributes(rules={
        'name': String(required=True),
    }),
])

address = Attributes(root_tag=True, )
b = Attributes()

blockquote = Attributes(root_tag=True, rules={
    'cite': Url(allow_anchor=True), 
})

br = Attributes(rules={
    'clear':  List(values=[
        'left', 'all', 'right', 'none', 
    ]),
})

caption = Attributes(allow_empty=True, rules={
    'align': List(values=[
        'top', 'bottom', 'left', 'right', 
    ]),
})

cite = Attributes()

div = Attributes(root_tag=True, rules={
    'style': attributes.style_display,
})

dl = Attributes(get_content=True, )

dt = Attributes(get_content=True, )

# fieldset = Attributes(root_tag=True, )
# ins = Attributes(root_tag=True, )
# del = Attributes(root_tag=True, )

h1 = Attributes(root_tag=True, rules={
    'align': text_align,
})

img = Attributes(rules={
    'title': string,
    'src': Url(required=True, allow_foriegn=False, tag='download_image'), 
    'alt': String(default=''),
    # Can enable: 'longdesc': Url(),
    'width': length,
    'height': length,
    'align': List(values=[
        'top', 'middle', 'bottom', 'left', 'right', 
    ]),
    'hspace': number,
    'vspace': number,
    'style': attributes.style,
    # Can enable: 'name': String(default=''),
})

li = Attributes(rules={
    'type': List(values=[
        'disc', 'square', 'circle', '1', 'a', 'A', 'i', 'I', 
    ]),
    'value': number,
})

ol = Attributes(root_tag=True, rules={
    'type': List(values=[
        '1', 'a', 'A', 'i', 'I', 
    ]),
    'start': number,
})

p = Attributes(root_tag=True, rules={
    # Can enable: 'align': text_align,
})

pre = Attributes(root_tag=True, )

span = Attributes(rules={
    'style': Style(rules={
        'text-decoration': List(values=[
            'underline', 'line-through', 
        ]),
    }),
})

table = Attributes(root_tag=True, rules={
    'title': string,
    'summary': string,
    'width': length,
    'border': number,
    'frame': List(values=[
        'void', 'above', 'below', 'hsides', 'lhs', 'rhs', 'vsides', 
        'box', 'border', 
    ]),
    'rules': List(values=[
        'none', 'groups', 'rows', 'cols', 'all', 
    ]), 
    'cellspacing': size,
    'cellpadding': size,
    'align': text_align,
    # Can enable: 'bgcolor': color,
    'style': attributes.style,
})

tbody = Attributes(rules={
    'align': List(values=[
        'left', 'center', 'right', 'justify', 'char', 
    ]),
    'char': char,
    'charoff': length,
    'valign': List(values=[
        'top', 'middle', 'bottom', 'baseline', 
    ]),
})

td = Attributes(default='&nbsp;', rules={
    # Can enable: 'headers': string,
    'abbr': string,
    'scope': List(values=[
        'row', 'col', 'rowgroup', 'colgroup', 
    ]),
    # Can enable: 'axis': string,
    'align': List(values=[
        'left', 'center', 'right', 'justify', 'char',
    ]),
    'char': char,
    'charoff': length,
    'valign': List(values=[
        'top', 'middle', 'bottom', 'baseline',
    ]),
    'rowspan': number,
    'colspan': number,
    'width': length,
    'height': length,
    # Can enable: 'nowrap': List(values=['', 'nowrap', ]),
    # Can enable: 'bgcolor': color,
    'style': attributes.style_td,
})

tr = Attributes(rules={
    'align': List(values=[
        'left', 'center', 'right', 'justify', 'char', 
    ]),
    'char': char,
    'charoff': length,
    'valign': List(values=[
        'top', 'middle', 'bottom', 'baseline',
    ]),
    # Can enable: 'bgcolor': color,
})

ul = Attributes(root_tag=True, rules={
    'type': List(values=[
        'disc', 'square', 'circle', 
    ]),
})
