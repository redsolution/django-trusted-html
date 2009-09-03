# -*- coding: utf-8 -*-

from trustedhtml.classes import Attributes, Or, String, Url
from trustedhtml.rules import values
from trustedhtml.rules import custom

a = Or(allow_empty=True, rules=[
    Attributes(rules={
        'title': values.title_a,
        # Can enable: 'charset': values.charset,
        # Can enable: 'type': values.content_type,
        'name': values.string,
        'href': values.href, 
        # Can enable: 'rel': values.link_type,    or     string,
        # Can enable: 'rev': values.link_type,    or     string,
        # Can enable: 'accesskey': char,
        # Can enable: 'shape':  List(values=['rect', 'circle', 'poly', 'default', ] ),
        # Can enable: 'coords': Sequence(validator=number, delimiter_regexp='\s*,\s*'),
        # Can enable: 'tabindex': number,
        'target': values.target, 
    }),
    Attributes(rules={
        'name': values.name_a,
    }),
])

address = Attributes(root_tag=True, )
b = Attributes()

blockquote = Attributes(root_tag=True, rules={
    'cite': values.cite, 
})

br = Attributes(rules={
    'clear':  values.clear,
})

caption = Attributes(allow_empty=True, rules={
    'align': values.align_caption,
})

cite = Attributes()

div = Attributes(root_tag=True, rules={
    'style': custom.values.style_div,
})

dl = Attributes(get_content=True, )

dt = Attributes(get_content=True, )

# fieldset = Attributes(root_tag=True, )
# ins = Attributes(root_tag=True, )
# del = Attributes(root_tag=True, )

h1 = Attributes(root_tag=True, rules={
    'align': values.align,
})

img = Attributes(rules={
    'title': values.string,
    'src': values.src, 
    'alt': values.alt,
    # Can enable: 'longdesc': Url(),
    'width': values.length,
    'height': values.length,
    'align': values.align_img,
    'hspace': values.number,
    'vspace': values.number,
    'style': values.style,
    # Can enable: 'name': String(default=''),
})

li = Attributes(rules={
    'type': values.type_li,
    'value': values.number,
})

ol = Attributes(root_tag=True, rules={
    'type': values.type_ol,
    'start': values.number,
})

p = Attributes(root_tag=True, rules={
    # Can enable: 'align': values.align,
})

pre = Attributes(root_tag=True, )

span = Attributes(rules={
    'style': custom.values.style_span,
})

table = Attributes(root_tag=True, rules={
    'title': values.string,
    'summary': values.string,
    'width': values.length,
    'border': values.number,
    'frame': values.frame,
    'rules': values.rules, 
#    'cellspacing': size,
#    'cellpadding': size,
    'align': values.align,
    # Can enable: 'bgcolor': color,
    'style': values.style,
})

tbody = Attributes(rules={
    'align': values.align_table,
    'char': values.char,
    'charoff': values.length,
    'valign': values.valign,
})

td = Attributes(default='&nbsp;', rules={
    # Can enable: 'headers': string,
    'abbr': values.string,
    'scope': values.scope,
    # Can enable: 'axis': string,
    'align': values.align_table,
    'char': values.char,
    'charoff': values.length,
    'valign': values.valign,
    'rowspan': values.number,
    'colspan': values.number,
    'width': values.length,
    'height': values.length,
    # Can enable: 'nowrap': List(values=['', 'nowrap', ]),
    # Can enable: 'bgcolor': color,
    'style': custom.values.style_td,
})

tr = Attributes(rules={
    'align': values.align_table,
    'char': values.char,
    'charoff': values.length,
    'valign': values.valign,
    # Can enable: 'bgcolor': color,
})

ul = Attributes(root_tag=True, rules={
    'type': values.type_ul,
})

#}, coreattrs = {
#    'id': string,
#    'title': values.string,
#    'class': string,
#    'style': values.style,
