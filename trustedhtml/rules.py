# -*- coding: utf-8 -*-

from trustedhtml.classes import *

align = TrustedList(values=[
    'left', 'right', 'center', 'justify', 
])

border_width = TrustedListOrSize(values=[
    'thin', 'medium', 'thick',
])

border_style = TrustedList(values=[
    'none', 'hidden', 'dotted', 'dashed', 'solid', 'double', 
    'groove', 'ridge', 'inset', 'outset', 
])

border = TrustedComplex(trusted_sequence=[
    border_width,
    border_style,
    TrustedColor(), 
])

style = TrustedStyle(trusted_list=[ {
    'border': border,
    'border-width': border_width,
    'border-style': border_style,
    'border-color': TrustedColor(),
    
    'margin': TrustedIndent(),
    'padding': TrustedIndent(),

    'margin-top': TrustedSize(),
    'padding-top': TrustedSize(),

    'width': TrustedSize(),
    'height': TrustedSize(),

    'float': TrustedList(values=[
        'left', 'right', 
    ]),
    'display': TrustedList(values=[
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

style_display = TrustedStyle(trusted_list=[ {
    'display': TrustedList(values=[
        'none'], invalid=True),
}, ])

style_td = TrustedStyle(trusted_list=[ {
    'border': border,
    'border-width': border_width,
    'border-style': border_style,
    'border-color': TrustedColor(),
    
    'margin': TrustedIndent(),
    'padding': TrustedIndent(),

    'margin-top': TrustedSize(),
    'padding-top': TrustedSize(),

    'width': TrustedSize(),
    'height': TrustedSize(),

    'white-space': TrustedList(values=[
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

link_type = TrustedList(values=[
    'alternate', 'stylesheet', 'start', 'next', 'prev', 
    'contents', 'index', 'glossary', 'copyright', 'chapter', 
    'section', 'subsection', 'appendix', 'help', 'bookmark',
] )

content_type = TrustedList(values=[
    'text/html', 'image/jpeg', 'image/png', 'image/gif', 'audio/mpeg', 'video/mpeg',    
    # Disabled: 'text/javascript', 'text/css', 
] ) # Full list: http://www.iana.org/assignments/media-types/

charset = TrustedList(values=[
    'utf-8', 'windows-1251', 'koi8-r', 'koi8-r', 'cp866', 'iso-8859-1', 'utf-16',
    # 'utf-7', # Disable (because of XSS)   
] ) # Full list: http://www.iana.org/assignments/character-sets

coreattrs = {
    'id': TrustedStr(),
    'title': TrustedStr(),
    'class': TrustedStr(),
    'style': style,
}

# For each tag-name you must specify list of attribute combinations:
# { <attribute-name>: <validation object> }
html = {
    'a': [ {
        'title': TrustedStr(required=''),
        # Can enable: 'charset': charset,
        # Can enable: 'type': content_type,
        'name': TrustedStr(),
        'href': TrustedUrl(allow_anchor=True, required=True), 
        # Can enable: 'rel': link_type,    or     TrustedStr(),
        # Can enable: 'rev': link_type,    or     TrustedStr(),
        # Can enable: 'accesskey': TrustedChr(),
        # Can enable: 'shape':  TrustedList(values=['rect', 'circle', 'poly', 'default', ] ),
        # Can enable: 'coords': TrustedSequence(validator=TrustedNumber(), delimiter_char=','),
        # Can enable: 'tabindex': TrustedNumber(),
        'target': TrustedList(values=['_blank', '_self', '_parent', '_top', ]), 
    }, { 
        'name': TrustedStr(required=True),
    } ],
    'address': [],
    'b': [],
    'blockquote': [{
        'cite': TrustedUrl(allow_anchor=True, required=False), 
    }, ],
    'br': [ {
        'clear':  TrustedList(values=[
            'left', 'all', 'right', 'none', 
        ]),
    }, ],
    'caption': [ {
        'align': TrustedList(values=[
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
        'title': TrustedStr(),
        'src': TrustedUrl(required=True, local_only=True, tag='download_image'), 
        'alt': TrustedStr(required=''),
        # Can enable: 'longdesc': TrustedUrl(),
        'width': TrustedLength(),
        'height': TrustedLength(),
        'align': TrustedList(values=[
            'top', 'middle', 'bottom', 'left', 'right', 
        ]),
        'hspace': TrustedNumber(),
        'vspace': TrustedNumber(),
        'style': style,
        # Can enable: 'name': TrustedStr(required=''),
    }, ],
    'li': [ {
        'type': TrustedList(values=[
            'disc', 'square', 'circle', '1', 'a', 'A', 'i', 'I', 
        ]),
        'value': TrustedNumber(),
    }, ],
    'ol': [ {
        'type': TrustedList(values=[
            '1', 'a', 'A', 'i', 'I', 
        ]),
        'start': TrustedNumber(),
    }, ],
    'p': [], # Can enable {'align': align,}
    'pre': [],
    'span': [ {
        'style': TrustedStyle(trusted_list=[ {
            'text-decoration': TrustedList(values=[
                'underline', 'line-through', 
            ]),
        }, ]),
    }, ],
    'table': [ {
        'title': TrustedStr(),
        'summary': TrustedStr(),
        'width': TrustedLength(),
        'border': TrustedNumber(),
        'frame': TrustedList(values=[
            'void', 'above', 'below', 'hsides', 'lhs', 'rhs', 'vsides', 
            'box', 'border', 
        ]),
        'rules': TrustedList(values=[
            'none', 'groups', 'rows', 'cols', 'all', 
        ]), 
        'cellspacing': TrustedSize(),
        'cellpadding': TrustedSize(),
        'align': align,
        # Can enable: 'bgcolor': TrustedColor(),
        'style': style,
    }, ],
    'tbody': [ {
        'align': TrustedList(values=[
            'left', 'center', 'right', 'justify', 'char', 
        ]),
        'char': TrustedChr(),
        'charoff': TrustedLength(),
        'valign': TrustedList(values=[
            'top', 'middle', 'bottom', 'baseline', 
        ]),
    }, ],
    'td': [ {
        # Can enable: 'headers': TrustedStr(),
        'abbr': TrustedStr(),
        'scope': TrustedList(values=[
            'row', 'col', 'rowgroup', 'colgroup', 
        ]),
        # Can enable: 'axis': TrustedStr(),
        'align': TrustedList(values=[
            'left', 'center', 'right', 'justify', 'char',
        ]),
        'char': TrustedChr(),
        'charoff': TrustedLength(),
        'valign': TrustedList(values=[
            'top', 'middle', 'bottom', 'baseline',
        ]),
        'rowspan': TrustedNumber(),
        'colspan': TrustedNumber(),
        'width': TrustedLength(),
        'height': TrustedLength(),
        # Can enable: 'nowrap': TrustedList(values=['', 'nowrap', ]),
        # Can enable: 'bgcolor': TrustedColor(),
        'style': style_td,
    }, ],
    'tr': [ {
        'align': TrustedList(values=[
            'left', 'center', 'right', 'justify', 'char', 
        ]),
        'char': TrustedChr(),
        'charoff': TrustedLength(),
        'valign': TrustedList(values=[
            'top', 'middle', 'bottom', 'baseline',
        ]),
        # Can enable: 'bgcolor': TrustedColor(),
    }, ],
    'ul': [ {
        'type': TrustedList(values=[
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
        'src': TrustedList(values=[smile_template % smile_name], required=True),
        'title': TrustedList(values=[smile_alt], required=smile_alt),
        'alt': TrustedList(values=[smile_alt], required=smile_alt),
    } for smile_name, smile_alt in smiles] + [
    {
        'src': TrustedList(values=[smile_template % smile_name], 
            required=smile_template % smile_name),
        'title': TrustedList(values=[smile_alt], required=True),
        'alt': TrustedList(values=[smile_alt], required=smile_alt),
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
        'type': TrustedList(values=[
            'disc', 'square', 'circle', '1', 'a', 'A', 'i', 'I',
        ]),
        'value': TrustedNumber(),
    }, ],
    'ol': [ {
        'type': TrustedList(values=[
            '1', 'a', 'A', 'i', 'I',
        ]),
        'start': TrustedNumber(),
    }, ],
    'p': [],
    'pre': [],
    'span': [ {
        'style': TrustedStyle(trusted_list=[ {
            'text-decoration': TrustedList(values=[
                'underline', 'line-through', 
            ]),
        }, ]),
    }, ],
    'strong': [],
    'sub': [],
    'sup': [],
    'u': [],
    'ul': [ {
        'type': TrustedList(values=[
            'disc', 'square', 'circle',
        ]),
    }, ],
}    
