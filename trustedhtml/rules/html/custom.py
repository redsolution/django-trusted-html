# -*- coding: utf-8 -*-

from trustedhtml.classes import Style, List

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
        # Can enable: 'coords': Sequence(validator=number, regexp=r'\s*,\s*'),
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
    # Can enable: 'longdesc': Uri(),
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





style_div = Style(rules={
    'display': List(values=[
        'none'], invalid=True),
})

style_span = Style(rules={
    'text-decoration': List(values=[
        'underline', 'line-through', 
    ]),
})

style_td = Style(rules={
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
})
#

#smiles = [
#    ('cool', u'Клёвый'),
#    ('cry', u'Плачет'),
#    ('embarassed', u'Обалдел'),
#    ('foot-in-mouth', u'Нога во рту'),
#    ('frown', u'Хмурый'),
#    ('innocent', u'Невинность'),
#    ('kiss', u'Поцелуй'),
#    ('laughing', u'Смеётся'),
#    ('money-mouth', u'Много денег'),
#    ('sealed', u'Запечатано'),
#    ('smile', u'Улыбается'),
#    ('surprised', u'Удивлён'),
#    ('tongue-out', u'Показывает язык'),
#    ('undecided', u'В нерешительности'),
#    ('wink', u'Подмигивает'),
#    ('yell', u'Вопит'),
#]
#
#smile_template = '/media/js/tiny_mce/plugins/emotions/img/smiley-%s.gif'
#
#smile_rules = [
#    {
#        'src': List(values=[smile_template % smile_name], required=True),
#        'title': List(values=[smile_alt], default=smile_alt),
#        'alt': List(values=[smile_alt], default=smile_alt),
#    } for smile_name, smile_alt in smiles] + [
#    {
#        'src': List(values=[smile_template % smile_name], 
#            default=smile_template % smile_name),
#        'title': List(values=[smile_alt], required=True),
#        'alt': List(values=[smile_alt], default=smile_alt),
#    } for smile_name, smile_alt in smiles]
#
#comment = {
#    'address': [],
#    'b': [],
#    'blockquote': [],
#    'cite': [],
#    'div': [ {
#        'style': style_display,
#    }, ],
#    'em': [],
#    'i': [],
#    'img': smile_rules,
#    'li': [ {
#        'type': List(values=[
#            'disc', 'square', 'circle', '1', 'a', 'A', 'i', 'I',
#        ]),
#        'value': number,
#    }, ],
#    'ol': [ {
#        'type': List(values=[
#            '1', 'a', 'A', 'i', 'I',
#        ]),
#        'start': number,
#    }, ],
#    'p': [],
#    'pre': [],
#    'span': [ {
#        'style': Style(rules={
#            'text-decoration': List(values=[
#                'underline', 'line-through', 
#            ]),
#        }),
#    }, ],
#    'strong': [],
#    'sub': [],
#    'sup': [],
#    'u': [],
#    'ul': [ {
#        'type': List(values=[
#            'disc', 'square', 'circle',
#        ]),
#    }, ],
#}    


full = Html(rules={
    'a': tags.a,
    'address': tags.address,
    'b': tags.b,
    'blockquote': tags.blockquote,
    'br': tags.br,
    'caption': tags.caption,
    'cite': tags.cite,
    'div': tags.div,
    'dl': tags.dl,
    'dt': tags.dt,
    'h1': tags.h1,
    'img': tags.img,
    'li': tags.li,
    'ol': tags.ol,
    'p': tags.p,
    'pre': tags.pre,
    'span': tags.span,
    'table': tags.table,
    'tbody': tags.tbody,
    'td': tags.td,
    'tr': tags.tr,
    'ul': tags.ul,
}
, equivalents = {
    'h1': [
        'h2', 'h3', 'h4', 'h5', 'h6',
    ],
    'b': [
        'em', 'i', 'strong', 'sub', 'sup', 'u',
    ],
    'td': [
        'th',
    ],
})
