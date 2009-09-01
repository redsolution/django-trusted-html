# -*- coding: utf-8 -*-

from trustedhtml.classes import *

string = String()
indent = Indent()
number = RegExp(regexp=r'([-+]?\d{1,7})$')
length = RegExp(regexp=r'([-+]?\d{1,7}%?)$')
size = RegExp(regexp=r'([-+]?\d{1,7}(%s))$' % '|'.join([
    '', 'px', '%', 'cm', 'mm', 'in', 'pt', 'pc', 'em', 'ex', 
]))
char = Char()
color = Or(rules=[
    List(values=[
        'activeborder', 'activecaption', 'appworkspace', 
        'background', 'buttonface', 'buttonhighlight', 'buttonshadow', 
        'buttontext', 'captiontext', 'graytext', 'highlight', 
        'highlighttext', 'inactiveborder', 'inactivecaption', 
        'inactivecaptiontext', 'infobackground', 'infotext', 'menu', 
        'menutext', 'scrollbar', 'threeddarkshadow', 'threedface', 
        'threedhighlight', 'threedlightshadow', 'threedshadow', 
        'window', 'windowframe', 'windowtext', 'currentcolor', 
    ] + [
        'aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure',  
        'beige', 'bisque', 'black', 'blanchedalmond', 'blue',
        'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse',
        'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson',
        'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray',
        'darkgreen', 'darkgrey', 'darkkhaki', 'darkmagenta',
        'darkolivegreen', 'darkorange', 'darkorchid', 'darkred',
        'darksalmon', 'darkseagreen', 'darkslateblue', 'darkslategray',
        'darkslategrey', 'darkturquoise', 'darkviolet', 'deeppink',
        'deepskyblue', 'dimgray', 'dimgrey', 'dodgerblue', 'firebrick',
        'floralwhite', 'forestgreen', 'fuchsia', 'gainsboro',
        'ghostwhite', 'gold', 'goldenrod', 'gray', 'green',
        'greenyellow', 'grey', 'honeydew', 'hotpink', 'indianred',
        'indigo', 'ivory', 'khaki', 'lavender', 'lavenderblush',
        'lawngreen', 'lemonchiffon', 'lightblue', 'lightcoral',
        'lightcyan', 'lightgoldenrodyellow', 'lightgray', 'lightgreen',
        'lightgrey', 'lightpink', 'lightsalmon', 'lightseagreen',
        'lightskyblue', 'lightslategray', 'lightslategrey',
        'lightsteelblue', 'lightyellow', 'lime', 'limegreen', 'linen',
        'magenta', 'maroon', 'mediumaquamarine', 'mediumblue',
        'mediumorchid', 'mediumpurple', 'mediumseagreen',
        'mediumslateblue', 'mediumspringgreen', 'mediumturquoise',
        'mediumvioletred', 'midnightblue', 'mintcream', 'mistyrose',
        'moccasin', 'navajowhite', 'navy', 'oldlace', 'olive',
        'olivedrab', 'orange', 'orangered', 'orchid', 'palegoldenrod',
        'palegreen', 'paleturquoise', 'palevioletred', 'papayawhip',
        'peachpuff', 'peru', 'pink', 'plum', 'powderblue', 'purple',
        'red', 'rosybrown', 'royalblue', 'saddlebrown', 'salmon',
        'sandybrown', 'seagreen', 'seashell', 'sienna', 'silver',
        'skyblue', 'slateblue', 'slategray', 'slategrey', 'snow',
        'springgreen', 'steelblue', 'tan', 'teal', 'thistle', 'tomato', 
        'turquoise', 'violet', 'wheat', 'white', 'whitesmoke',
        'yellow', 'yellowgreen', 
    ]),
    RegExp(regexp=
        '((rgb|hsl)\(%(w)s%(num)s%%?%(w)s\,%(w)s%(num)s%%?%(w)s\,%(w)s%(num)s%%?%(w)s\))|'
        '((rgba|hsla)\(%(w)s%(num)s%%?%(w)s\,%(w)s%(num)s%%?%(w)s\,%(w)s%(num)s%%?%(w)s,%(w)s%(num)s%%(w)s\))|'
        '(#%(h)s{6})|(#%(h)s{3}))' % {
            'h': '[0-9a-f]',
            'w': '[ \t\n]*',
            'num': '{d}+|{d}*\.{d}+',
        }
    ),
])

# TODO: remove_it vs get_content

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
        'title': String(default=''),
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
        'cite': Url(allow_anchor=True), 
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
        'style': style,
        # Can enable: 'name': String(default=''),
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
