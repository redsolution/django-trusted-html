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
number = RegExp(regexp=r'([-+]?\d{1,7})$')
length = RegExp(regexp=r'([-+]?\d{1,7}%?)$')
size = RegExp(regexp=r'([-+]?\d{1,7}(%s))$' % '|'.join([
    '', 'px', '%', 'cm', 'mm', 'in', 'pt', 'pc', 'em', 'ex', 
]))
indent = Sequence(rule=size, min_split=1, max_split=4)
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
