# -*- coding: utf-8 -*-

from trustedhtml.classes import *

lexic_dict = {}
lexic_dict['h'] = r'[0-9a-f]' % lexic_dict
lexic_dict['nonascii'] = r'[\200-\4177777]' % lexic_dict
lexic_dict['unicode'] = r'\\%(h)s{1,6}[ \t\r\n\f]?' % lexic_dict
lexic_dict['escape'] = r'%(unicode)s|\\[ -~\200-\4177777]' % lexic_dict
lexic_dict['nmstart'] = r'[a-z]|%(nonascii)s|%(escape)s' % lexic_dict
lexic_dict['nmchar'] = r'[a-z0-9-]|%(nonascii)s|%(escape)s' % lexic_dict
lexic_dict['string1'] = r'\"([\t !#$%%&(-~]|\\%(nl)s|\'|%(nonascii)s|%(escape)s)*\"' % lexic_dict
lexic_dict['string2'] = r'\'([\t !#$%%&(-~]|\\%(nl)s|\"|%(nonascii)s|%(escape)s)*\'' % lexic_dict

lexic_dict['ident'] = r'%(nmstart)s%(nmchar)s*' % lexic_dict
lexic_dict['name'] = r'%(nmchar)s+' % lexic_dict
lexic_dict['num'] = r'[0-9]+|[0-9]*\.[0-9]+' % lexic_dict
lexic_dict['string'] = r'%(string1)s|%(string2)s' % lexic_dict
lexic_dict['url'] = r'([!#$%%&*-~]|%(nonascii)s|%(escape)s)*' % lexic_dict
lexic_dict['w'] = r'[ \t\r\n\f]*' % lexic_dict
lexic_dict['nl'] = r'\n|\r\n|\r|\f' % lexic_dict
lexic_dict['range'] = r'\?{1,6}|%(h)s(\?{0,5}|%(h)s(\?{0,4}|%(h)s(\?{0,3}|%(h)s(\?{0,2}|%(h)s(\??|%(h)s)))))' % lexic_dict


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
        '(((rgb|hsl)\(%(w)s%(num)s%%?%(w)s\,%(w)s%(num)s%%?%(w)s\,%(w)s%(num)s%%?%(w)s\))|'
        '((rgba|hsla)\(%(w)s%(num)s%%?%(w)s\,%(w)s%(num)s%%?%(w)s\,%(w)s%(num)s%%?%(w)s,%(w)s%(num)s%%(w)s\))|'
        '(#%(h)s{6})|(#%(h)s{3})))$' % lexic_dict
    ),
])

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

#coreattrs = {
#    'id': string,
#    'title': string,
#    'class': string,
#    'style': style,
#}

a = Or(rules=[
    Tag(attributes={
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
    }),
    Tag(attributes={
        'name': String(required=True),
    }),
])

address = Tag()
b = Tag()

blockquote = Tag(attributes={
    'cite': Url(allow_anchor=True), 
})

br = Tag(attributes={
    'clear':  List(values=[
        'left', 'all', 'right', 'none', 
    ]),
})

caption = Tag(attributes={
    'align': List(values=[
        'top', 'bottom', 'left', 'right', 
    ]),
})

cite = Tag()

div = Tag(attributes={
        'style': style_display,
})

# dt = Tag(get_content=True)

h1 = Tag(attributes={
        'align': text_align,
})

img = Tag(attributes={
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
})

li = Tag(attributes={
        'type': List(values=[
            'disc', 'square', 'circle', '1', 'a', 'A', 'i', 'I', 
        ]),
        'value': number,
})

ol = Tag(attributes={
        'type': List(values=[
            '1', 'a', 'A', 'i', 'I', 
        ]),
        'start': number,
})

p = Tag(attributes={
    # Can enable: 'align': text_align,
})

pre = Tag()

span = Tag(attributes={
        'style': Style(trusted_list=[ {
            'text-decoration': List(values=[
                'underline', 'line-through', 
            ]),
        }, ]),
})

table = Tag(attributes={
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
})

tbody = Tag(attributes={
        'align': List(values=[
            'left', 'center', 'right', 'justify', 'char', 
        ]),
        'char': char,
        'charoff': length,
        'valign': List(values=[
            'top', 'middle', 'bottom', 'baseline', 
        ]),
})

td = Tag(attributes={
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
})

tr = Tag(attributes={
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

ul = Tag(attributes={
        'type': List(values=[
            'disc', 'square', 'circle', 
        ]),
})


# For each tag-name you must specify list of attribute combinations:
# { <attribute-name>: <validation object> }
html = Html(tags={
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
})
