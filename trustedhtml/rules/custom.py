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
        'title': List(values=[smile_alt], default=smile_alt),
        'alt': List(values=[smile_alt], default=smile_alt),
    } for smile_name, smile_alt in smiles] + [
    {
        'src': List(values=[smile_template % smile_name], 
            default=smile_template % smile_name),
        'title': List(values=[smile_alt], required=True),
        'alt': List(values=[smile_alt], default=smile_alt),
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
