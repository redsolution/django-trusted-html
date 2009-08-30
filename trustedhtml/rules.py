# -*- coding: utf-8 -*-

from trustedhtml.classes import *

string = String()
indent = Indent()
number = Number()
size = Size()
length = Length()
char = Char()
color = Color()

align = List(values=[
    'left', 'right', 'center', 'justify', 
])

border_width = ListOrSize(values=[
    'thin', 'medium', 'thick',
])

border_style = List(values=[
    'none', 'hidden', 'dotted', 'dashed', 'solid', 'double', 
    'groove', 'ridge', 'inset', 'outset', 
])

border_complex = Complex(trusted_sequence=[
    border_width,
    border_style,
    color,
])

style = Style(trusted_list=[ {
    'border': border_complex,
    'border-width': border_width,
    'border-style': border_style,
    'border-color': color,
    
    'margin': indent,
    'padding': indent,

    'margin-top': size,
    'padding-top': size,

    'width': size,
    'height': size,

    'float': List(values=[
        'left', 'right', 
    ]),
    'display': List(values=[
        'none'], invalid=True),
}, ], equivalents = {
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
    'margin-top': [
        'margin-bottom', 'margin-left', 'margin-right',
    ],
    'padding-top': [
        'padding-bottom', 'padding-left', 'padding-right',
    ],
})

style_display = Style(trusted_list=[ {
    'display': List(values=[
        'none'], invalid=True),
}, ])

style_td = Style(trusted_list=[ {
    'border': border_complex,
    'border-width': border_width,
    'border-style': border_style,
    'border-color': color,
    
    'margin': indent,
    'padding': indent,

    'margin-top': size,
    'padding-top': size,

    'width': size,
    'height': size,

    'white-space': List(values=[
        'pre', 'nowrap', 'normal', 
    ]),
}, ], equivalents = {
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
    'margin-top': [
        'margin-bottom', 'margin-left', 'margin-right',
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

coreattrs = {
    'id': string,
    'title': string,
    'class': string,
    'style': style,
}

# For each tag-name you must specify list of attribute combinations:
# { <attribute-name>: <validation object> }
html = {
    'a': [ {
        'title': String(required=''),
        # Can enable: 'charset': charset,
        # Can enable: 'type': content_type,
        'name': string,
        'href': Url(allow_anchor=True, required=True), 
        # Can enable: 'rel': link_type,    or     string,
        # Can enable: 'rev': link_type,    or     string,
        # Can enable: 'accesskey': char,
        # Can enable: 'shape':  List(values=['rect', 'circle', 'poly', 'default', ] ),
        # Can enable: 'coords': Sequence(validator=number, delimiter_char=','),
        # Can enable: 'tabindex': number,
        'target': List(values=['_blank', '_self', '_parent', '_top', ]), 
    }, { 
        'name': String(required=True),
    } ],
    'address': [],
    'b': [],
    'blockquote': [{
        'cite': Url(allow_anchor=True, required=False), 
    }, ],
    'br': [ {
        'clear':  List(values=[
            'left', 'all', 'right', 'none', 
        ]),
    }, ],
    'caption': [ {
        'align': List(values=[
            'top', 'bottom', 'left', 'right', 
        ]),
    }, ],
    'cite': [],
    'div': [ {
        'style': style_display,
    }, ],
    'h1': [ {
        'align': align,
    }, ],
    'img': [ {
        'title': string,
        'src': Url(required=True, local_only=True, tag='download_image'), 
        'alt': String(required=''),
        # Can enable: 'longdesc': Url(),
        'width': length,
        'height': length,
        'align': List(values=[
            'top', 'middle', 'bottom', 'left', 'right', 
        ]),
        'hspace': number,
        'vspace': number,
        'style': style,
        # Can enable: 'name': String(required=''),
    }, ],
    'li': [ {
        'type': List(values=[
            'disc', 'square', 'circle', '1', 'a', 'A', 'i', 'I', 
        ]),
        'value': number,
    }, ],
    'ol': [ {
        'type': List(values=[
            '1', 'a', 'A', 'i', 'I', 
        ]),
        'start': number,
    }, ],
    'p': [], # Can enable {'align': align,}
    'pre': [],
    'span': [ {
        'style': Style(trusted_list=[ {
            'text-decoration': List(values=[
                'underline', 'line-through', 
            ]),
        }, ]),
    }, ],
    'table': [ {
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
        'align': align,
        # Can enable: 'bgcolor': color,
        'style': style,
    }, ],
    'tbody': [ {
        'align': List(values=[
            'left', 'center', 'right', 'justify', 'char', 
        ]),
        'char': char,
        'charoff': length,
        'valign': List(values=[
            'top', 'middle', 'bottom', 'baseline', 
        ]),
    }, ],
    'td': [ {
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
        'style': style_td,
    }, ],
    'tr': [ {
        'align': List(values=[
            'left', 'center', 'right', 'justify', 'char', 
        ]),
        'char': char,
        'charoff': length,
        'valign': List(values=[
            'top', 'middle', 'bottom', 'baseline',
        ]),
        # Can enable: 'bgcolor': color,
    }, ],
    'ul': [ {
        'type': List(values=[
            'disc', 'square', 'circle', 
        ]),
    }, ]
}
#, equivalents = {
#    'h1': [
#        'h2', 'h3', 'h4', 'h5', 'h6',
#    ],
#    'b': [
#        'em', 'i', 'strong', 'sub', 'sup', 'u',
#    ],
#}


smiles = [
    ('cool', u'Клёвый'),
    ('cry', u'Плачет'),
    ('embarassed', u'Обалдел'),
    ('foot-in-mouth', u'Нога во рту'),
    ('frown', u'Хмурый'),
    ('innocent', u'Невинность'),
    ('kiss', u'Поцелуй'),
    ('laughing', u'Смеётся'),
    ('money-mouth', u'Много денег'),
    ('sealed', u'Запечатано'),
    ('smile', u'Улыбается'),
    ('surprised', u'Удивлён'),
    ('tongue-out', u'Показывает язык'),
    ('undecided', u'В нерешительности'),
    ('wink', u'Подмигивает'),
    ('yell', u'Вопит'),
]

smile_template = '/media/js/tiny_mce/plugins/emotions/img/smiley-%s.gif'

smile_rules = [
    {
        'src': List(values=[smile_template % smile_name], required=True),
        'title': List(values=[smile_alt], required=smile_alt),
        'alt': List(values=[smile_alt], required=smile_alt),
    } for smile_name, smile_alt in smiles] + [
    {
        'src': List(values=[smile_template % smile_name], 
            required=smile_template % smile_name),
        'title': List(values=[smile_alt], required=True),
        'alt': List(values=[smile_alt], required=smile_alt),
    } for smile_name, smile_alt in smiles]

comment = {
    'address': [],
    'b': [],
    'blockquote': [],
    'cite': [],
    'div': [ {
        'style': style_display,
    }, ],
    'em': [],
    'i': [],
    'img': smile_rules,
    'li': [ {
        'type': List(values=[
            'disc', 'square', 'circle', '1', 'a', 'A', 'i', 'I',
        ]),
        'value': number,
    }, ],
    'ol': [ {
        'type': List(values=[
            '1', 'a', 'A', 'i', 'I',
        ]),
        'start': number,
    }, ],
    'p': [],
    'pre': [],
    'span': [ {
        'style': Style(trusted_list=[ {
            'text-decoration': List(values=[
                'underline', 'line-through', 
            ]),
        }, ]),
    }, ],
    'strong': [],
    'sub': [],
    'sup': [],
    'u': [],
    'ul': [ {
        'type': List(values=[
            'disc', 'square', 'circle',
        ]),
    }, ],
}    
