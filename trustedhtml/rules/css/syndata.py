"""
CSS2 syntax and basic data types
http://www.w3.org/TR/1998/REC-CSS2-19980512/syndata.html
"""

from trustedhtml.classes import List, RegExp, Uri, Or, And
from trustedhtml.rules.css.grammar import grammar

number = RegExp(regexp=r'%(num)s$' % grammar)
length = RegExp(regexp=r'%(length)s$' % grammar)
percentage = RegExp(regexp=r'%(percentage)s$' % grammar)
integer = RegExp(regexp=r'%(int)s$' % grammar)

positive_number = RegExp(regexp=r'%(positive-num)s$' % grammar)
positive_length = RegExp(regexp=r'%(positive-length)s$' % grammar)
positive_percentage = RegExp(regexp=r'%(positive-percentage)s$' % grammar)
positive_integer = RegExp(regexp=r'%(positive-int)s$' % grammar)

identifier = RegExp(regexp=r'%(ident)s$' % grammar)

string = RegExp(regexp=r'%(string)s$' % grammar)

#Not used
#angle = RegExp(regexp=r'(%(num)s(deg|rad|grad))$' % grammar)
#time = RegExp(regexp=r'(%(positive-num)s(ms|s))$' % grammar)
#freq = RegExp(regexp=r'(%(positive-num)s(hz|khz))$' % grammar)
#dimen = RegExp(regexp=r'(%(num)s%(ident)s)$' % grammar)

color_spec = RegExp(
    regexp=r'(?P<n>rgb|hsl)\('
        '%(w)s(?P<a>%(int)s%%?)%(w)s\,'
        '%(w)s(?P<b>%(int)s%%?)%(w)s\,'
        '%(w)s(?P<c>%(int)s%%?)%(w)s\)$' % grammar,
    expand=r'\g<n>(\g<a>,\g<b>,\g<c>)',
)
color_alpha = RegExp(
    regexp=r'(?P<n>rgba|hsla)\('
        '%(w)s(?P<a>%(int)s%%?)%(w)s\,'
        '%(w)s(?P<b>%(int)s%%?)%(w)s\,'
        '%(w)s(?P<c>%(int)s%%?)%(w)s\,'
        '%(w)s(?P<d>%(int)s%%?)%(w)s\)$' % grammar,
    expand=r'\g<n>(\g<a>,\g<b>,\g<c>,\g<d>)',
)
color_hex = RegExp(regexp=r'(#%(h)s{3}|#%(h)s{6})$' % grammar,)
color_list = List(values=[
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
])

color = Or(rules=[
    color_list,
    color_spec,
    color_alpha,
    color_hex,
])

uri_base = Uri()
uri_image = Uri(type=Uri.IMAGE)
uri_string1_in = RegExp(
    regexp=r'url\(%(w)s(%(string1)s)%(w)s\)' % grammar,
    expand=r'\g<string1>',
)
uri_string1_out = RegExp(
    regexp=r'(.*)$',
    expand='url(\"\\1\")',
)
uri_string2_in = RegExp(
    regexp=r'url\(%(w)s(%(string2)s)%(w)s\)' % grammar,
    expand=r'\g<string2>',
)
uri_string2_out = RegExp(
    regexp=r'(.*)$',
    expand='url(\'\\1\')',
)
uri_url_in = RegExp(
    regexp=r'url\(%(w)s%(url)s%(w)s\)' % grammar,
    expand=r'\g<url>',
)
uri_url_out = RegExp(
    regexp=r'(.*)$',
    expand='url(\\1)',
)

uri = Or(rules=[
    And(rules=[
        uri_string1_in, uri_base, uri_string1_out,
    ]),
    And(rules=[
        uri_string2_in, uri_base, uri_string2_out,
    ]),
    And(rules=[
        uri_url_in, uri_base, uri_url_out,
    ]),
])

uri_image = Or(rules=[
    And(rules=[
        uri_string1_in, uri_image, uri_string1_out,
    ]),
    And(rules=[
        uri_string2_in, uri_image, uri_string2_out,
    ]),
    And(rules=[
        uri_url_in, uri_image, uri_url_out,
    ]),
])
