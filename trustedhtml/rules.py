# -*- coding: utf-8 -*-

from trustedhtml.classes import *

string = String()
indent = Indent()
number = Number()
size = Size()
length = Length()
char = Char()
color = Color()

# TODO: remove_it vs get_content

# TODO: add it to Style
core_css_values = [
    'inherit',
]

# TODO: css_url = Url(css=True, values=['none'])
css_url = String()

background_attachment = List(values=[
    'scroll', 'fixed',
])

#background_color = Color(values=[
#    'transparent',
#])
background_color = color

background_image = css_url

background_position_x = ListOrSize(values=[
    'left', 'center', 'right', 
])

background_position_y = ListOrSize(values=[
    'top', 'center', 'bottom', 
])

background_position = Complex(trusted_sequence=[
    background_position_x,
    background_position_y,
])

background_repeat = List(values=[
    'repeat', 'repeat-x', 'repeat-y', 'no-repeat', 
])

background = Complex(trusted_sequence=[
    background_color,
    background_image,
    background_repeat,
    background_attachment,
    background_position,
])

#border_color = Color(values=[
#    'transparent',
#])
border_color = color

border_style = List(values=[
    'none', 'hidden', 'dotted', 'dashed', 'solid', 'double', 
    'groove', 'ridge', 'inset', 'outset', 
])

border_width = ListOrSize(values=[
    'thin', 'medium', 'thick',
])

border_complex = Complex(trusted_sequence=[
    border_width,
    border_style,
    border_color,
])

border_collapse = List(values=[
    'collapse', 'separate',
])

border_spacing = Complex(trusted_sequence=[
    size,
    size,
])

bottom = ListOrSize(values=[
    'auto',
])

caption_side = List(values=[
    'top', 'bottom',
])

clear = List(values=[
    'left', 'right', 'both', 'none', 
])

# TODO: rect(top, right, bottom, left) | auto
clip = String()

cursor = List(values=[
    'auto', 'crosshair', 'default', 'e-resize', 'help', 'move', 'n-resize', 
    'ne-resize', 'nw-resize', 'pointer', 'progress', 's-resize', 'se-resize',
    'sw-resize', 'text', 'w-resize', 'wait',
])
# Don`t support URLs for cursor

direction = List(values=[
    'ltr', 'rtl',
])

display = List(values=[
    'none', 'block', 'inline', 'inline-block', 'inline-table', 'list-item',
    'run-in', 'table', 'table-caption', 'table-cell', 'table-column',
    'table-column-group', 'table-footer-group', 'table-header-group',
    'table-row', 'table-row-group',
])

empty_cells = List(values=[
    'hide', 'show', 
])

float = List(values=[
    'left', 'right', 
])

# TODO: font_family = String(without_spaces=True)
font_family = String()

font_size = ListOrSize(values=[
    'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large',
    'smaller', 'larger',
])

font_style = List(values=[
    'normal', 'italic', 'oblique',
])

font_variant = List(values=[
    'normal', 'small-caps',
])

font_weight = List(values=[
    'normal', 'bold', 'bolder', 'lighter',
    '100', '200', '300', '400', '500', '600', '700', '800', '900',
])

line_height = ListOrSize(values=[
    'normal'
])

font = Complex(trusted_sequence=[
    font_style,
    font_variant,
    font_weight,
    font_size,
    line_height,
    font_family,
    List(values=[
        'caption', 'icon', 'menu', 'message-box', 'small-caption', 'status-bar',
    ])
])

letter_spacing = ListOrSize(values=[
    'normal'
])

list_style_image = css_url

list_style_position = List(values=[
    'inside', 'outside'
])

list_style_type = List(values=[
    'none', 'circle', 'disc', 'square', 'armenian', 'decimal',
    'decimal-leading-zero', 'georgian', 'lower-alpha', 'lower-greek',
    'lower-latin', 'lower-roman', 'upper-alpha', 'upper-latin', 'upper-roman'
])

list_style = Complex(trusted_sequence=[
    list_style_type,
    list_style_position,
    list_style_image,
])

#margin = Indent(failback=
#    List(values=[
#        'auto'
#    ])
#)

margin = Indent()

margin_top = ListOrSize(values=[
    'auto'
])

max_height = ListOrSize(values=[
    'none'
])

#outline_color = Color(values=[
#    'invert',
#])
outline_color = color

outline_style = List(values=[
    'none', 'dotted', 'dashed', 'solid', 'double', 
    'groove', 'ridge', 'inset', 'outset', 
])

outline_width = border_width

outline_complex = Complex(trusted_sequence=[
    outline_color,
    outline_style,
    outline_width,
])

overflow = List(values=[
    'visible', 'hidden', 'scroll', 'auto',
])

page_break_after = List(values=[
    'auto', 'always', 'avoid', 'left', 'right',
])

page_break_inside = List(values=[
    'auto', 'avoid',
])

padding = Indent()

padding_top = Size()

position = List(values=[
    'absolute', 'fixed', 'relative', 'static',
])

# none | string string string string
quotes = String()

table_layout = List(values=[
    'auto', 'fixed',
])

text_align = List(values=[
    'left', 'right', 'center', 'justify', 
])

text_decoration = List(values=[
    'none', 'underline', 'overline', 'line-through', 'blink', 
])

text_indent = Size()

text_transform = List(values=[
    'none', 'capitalize', 'uppercase', 'lowercase', 
])

vertical_align = ListOrSize(values=[
    'baseline', 'sub', 'super', 'top', 'text-top', 'middle', 'bottom', 'text-bottom',
])

visibility = List(values=[
    'visible', 'hidden', 'collapse',
])

white_space = List(values=[
    'normal', 'nowrap', 'pre', 'pre-line', 'pre-wrap',
])

#z-index = List(values=[
#    'auto'
#], failback=Number())
z_index = number

style = Style(trusted_list=[ {
    'background': background,
    'background-color': background_color,
    'background-image': background_image,
    'background-repeat': background_repeat,
    'background-attachment': background_attachment,
    'background-position': background_position,
    
    'border': border_complex,
    'border-width': border_width,
    'border-style': border_style,
    'border-color': color,
    'border-collapse': border_collapse,
    
    'bottom': bottom,
    'clear': clear,
    'color': color,
    
    # content is big security hole
    #'content':
    #'counter-increment': 
    #'counter-reset': 
    
    'margin': margin,
    'margin-top': margin_top,

    'padding': padding,
    'padding-top': padding_top,

    'width': size,
    'height': size,

    'float': float,
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
        'align': text_align,
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
    'p': [], # Can enable {'align': text_align,}
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
        'align': text_align,
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
