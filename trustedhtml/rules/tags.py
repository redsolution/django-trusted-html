# -*- coding: utf-8 -*-

from trustedhtml.classes import *
from trustedhtml.rules.common import *
from trustedhtml.rules import attributes

a = Or(rules=[
    Tag(rules={
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
    Tag(rules={
        'name': String(required=True),
    }),
])

address = Tag()
b = Tag()

blockquote = Tag(rules={
    'cite': Url(allow_anchor=True), 
})

br = Tag(rules={
    'clear':  List(values=[
        'left', 'all', 'right', 'none', 
    ]),
})

caption = Tag(rules={
    'align': List(values=[
        'top', 'bottom', 'left', 'right', 
    ]),
})

cite = Tag()

div = Tag(rules={
    'style': attributes.style_display,
})

# dt = Tag(get_content=True)

h1 = Tag(rules={
    'align': text_align,
})

img = Tag(rules={
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

li = Tag(rules={
    'type': List(values=[
        'disc', 'square', 'circle', '1', 'a', 'A', 'i', 'I', 
    ]),
    'value': number,
})

ol = Tag(rules={
    'type': List(values=[
        '1', 'a', 'A', 'i', 'I', 
    ]),
    'start': number,
})

p = Tag(rules={
    # Can enable: 'align': text_align,
})

pre = Tag()

span = Tag(rules={
    'style': Style(rules={
        'text-decoration': List(values=[
            'underline', 'line-through', 
        ]),
    }),
})

table = Tag(rules={
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

tbody = Tag(rules={
    'align': List(values=[
        'left', 'center', 'right', 'justify', 'char', 
    ]),
    'char': char,
    'charoff': length,
    'valign': List(values=[
        'top', 'middle', 'bottom', 'baseline', 
    ]),
})

td = Tag(rules={
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

tr = Tag(rules={
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

ul = Tag(rules={
    'type': List(values=[
        'disc', 'square', 'circle', 
    ]),
})


# For each tag-name you must specify list of attribute combinations:
# { <attribute-name>: <validation object> }
html = Html(rules={
    'a': a,
    'address': address,
    'b': b,
    'blockquote': blockquote,
    'br': br,
    'caption': caption,
    'cite': cite,
    'div': div,
    'h1': h1,
    'img': img,
    'li': li,
    'ol': ol,
    'p': p,
    'pre': pre,
    'span': span,
    'table': table,
    'tbody': tbody,
    'td': td,
    'tr': tr,
    'ul': ul,
}
, equivalents = {
    'h1': [
        'h2', 'h3', 'h4', 'h5', 'h6',
    ],
    'b': [
        'em', 'i', 'strong', 'sub', 'sup', 'u',
    ],
#}, coreattrs = {
#    'id': string,
#    'title': string,
#    'class': string,
#    'style': attributes.style,
})
