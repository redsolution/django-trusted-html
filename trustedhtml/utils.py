"""Utils used by classes"""

import re

SGML_CHARACTER_ENTITIES={
    'nbsp': 160,
    'iexcl': 161,
    'cent': 162,
    'pound': 163,
    'curren': 164,
    'yen': 165,
    'brvbar': 166,
    'sect': 167,
    'uml': 168,
    'copy': 169,
    'ordf': 170,
    'laquo': 171,
    'not': 172,
    'shy': 173,
    'reg': 174,
    'macr': 175,
    'deg': 176,
    'plusmn': 177,
    'sup2': 178,
    'sup3': 179,
    'acute': 180,
    'micro': 181,
    'para': 182,
    'middot': 183,
    'cedil': 184,
    'sup1': 185,
    'ordm': 186,
    'raquo': 187,
    'frac14': 188,
    'frac12': 189,
    'frac34': 190,
    'iquest': 191,
    'Agrave': 192,
    'Aacute': 193,
    'Acirc': 194,
    'Atilde': 195,
    'Auml': 196,
    'Aring': 197,
    'AElig': 198,
    'Ccedil': 199,
    'Egrave': 200,
    'Eacute': 201,
    'Ecirc': 202,
    'Euml': 203,
    'Igrave': 204,
    'Iacute': 205,
    'Icirc': 206,
    'Iuml': 207,
    'ETH': 208,
    'Ntilde': 209,
    'Ograve': 210,
    'Oacute': 211,
    'Ocirc': 212,
    'Otilde': 213,
    'Ouml': 214,
    'times': 215,
    'Oslash': 216,
    'Ugrave': 217,
    'Uacute': 218,
    'Ucirc': 219,
    'Uuml': 220,
    'Yacute': 221,
    'THORN': 222,
    'szlig': 223,
    'agrave': 224,
    'aacute': 225,
    'acirc': 226,
    'atilde': 227,
    'auml': 228,
    'aring': 229,
    'aelig': 230,
    'ccedil': 231,
    'egrave': 232,
    'eacute': 233,
    'ecirc': 234,
    'euml': 235,
    'igrave': 236,
    'iacute': 237,
    'icirc': 238,
    'iuml': 239,
    'eth': 240,
    'ntilde': 241,
    'ograve': 242,
    'oacute': 243,
    'ocirc': 244,
    'otilde': 245,
    'ouml': 246,
    'divide': 247,
    'oslash': 248,
    'ugrave': 249,
    'uacute': 250,
    'ucirc': 251,
    'uuml': 252,
    'yacute': 253,
    'thorn': 254,
    'yuml': 255,
    # Latin Extended-B
    'fnof': 402,
    # C0 Controls and Basic Latin
    'quot': 34,
    'amp': 38,
    'lt': 60,
    'gt': 62,
    # Latin Extended-A
    'OElig': 338,
    'oelig': 339,
    'Scaron': 352,
    'scaron': 353,
    'Yuml': 376,
    # Spacing Modifier Letters
    'circ': 710,
    'tilde': 732,
    # General Punctuation
    'ensp': 8194,
    'emsp': 8195,
    'thinsp': 8201,
    'zwnj': 8204,
    'zwj': 8205,
    'lrm': 8206,
    'rlm': 8207,
    'ndash': 8211,
    'mdash': 8212,
    'lsquo': 8216,
    'rsquo': 8217,
    'sbquo': 8218,
    'ldquo': 8220,
    'rdquo': 8221,
    'bdquo': 8222,
    'dagger': 8224,
    'Dagger': 8225,
    'permil': 8240,
    'lsaquo': 8249,
    'rsaquo': 8250,
    'euro': 8364,
    'mu': 956,
    'nu': 957,
    'xi': 958,
    'omicron': 959,
    'pi': 960,
    'rho': 961,
    'sigmaf': 962,
    'sigma': 963,
    'tau': 964,
    'upsilon': 965,
    'phi': 966,
    'chi': 967,
    'psi': 968,
    'omega': 969,
    'thetasym': 977,
    'upsih': 978,
    'piv': 982,
    # General Punctuation
    'bull': 8226,
    'hellip': 8230,
    'prime': 8242,
    'Prime': 8243,
    'oline': 8254,
    'frasl': 8260,
    # Letterlike Symbols
    'weierp': 8472,
    'image': 8465,
    'real': 8476,
    'trade': 8482,
    'alefsym': 8501,
    # Arrows
    'larr': 8592,
    'uarr': 8593,
    'rarr': 8594,
    'darr': 8595,
    'harr': 8596,
    'crarr': 8629,
    'lArr': 8656,
    'uArr': 8657,
    'rArr': 8658,
    'dArr': 8659,
    'hArr': 8660,
    # Mathematical Operators
    'forall': 8704,
    'part': 8706,
    'exist': 8707,
    'empty': 8709,
    'nabla': 8711,
    'isin': 8712,
    'notin': 8713,
    'ni': 8715,
    'prod': 8719,
    'sum': 8721,
    'minus': 8722,
    'lowast': 8727,
    'radic': 8730,
    'prop': 8733,
    'infin': 8734,
    'ang': 8736,
    'and': 8743,
    'or': 8744,
    'cap': 8745,
    'cup': 8746,
    'int': 8747,
    'there4': 8756,
    'sim': 8764,
    'cong': 8773,
    'asymp': 8776,
    'ne': 8800,
    'equiv': 8801,
    'le': 8804,
    'ge': 8805,
    'sub': 8834,
    'sup': 8835,
    'nsub': 8836,
    'sube': 8838,
    'supe': 8839,
    'oplus': 8853,
    'otimes': 8855,
    'perp': 8869,
    'sdot': 8901,
    # Miscellaneous Technical
    'lceil': 8968,
    'rceil': 8969,
    'lfloor': 8970,
    'rfloor': 8971,
    'lang': 9001,
    'rang': 9002,
    # Geometric Shapes
    'loz': 9674,
    # Miscellaneous Symbols
    'spades': 9824,
    'clubs': 9827,
    'hearts': 9829,
    'diams': 9830,
}
# Character entity references in HTML 4
# http://www.w3.org/TR/REC-html40/sgml/entities.html
# Entities` names was lower cased.

SGML_CHARACTER_RE = re.compile(r'(?P<string>&(#(?P<dec>[0-9]+)|#x(?P<hex>[0-9A-Fa-f]+)|(?P<name>[a-zA-Z][a-zA-Z0-9]*));?)')
def SGML_CHARACTER_REPL(match):
    """Replace character entity with character"""
    dict = match.groupdict()
    try:
        if dict['dec']:
            code = int(dict['dec'])
        elif dict['hex']:
            code = int(dict['hex'], 16)
        elif dict['name']:
            code = SGML_CHARACTER_ENTITIES[dict['name'].lower()]
        else:
            raise ValueError
        return unichr(code)
    except (ValueError, KeyError, OverflowError):
        return dict['string']

SGML_SPACE_RE = re.compile(r'[\n\r\t]')
SGML_SPACE_REPL = ''

def get_cdata(value):
    """
    Return valid CDATA:
        Replace character entities with characters,
        Ignore line feeds,
        Replace each carriage return or tab with a single space.

    http://www.w3.org/TR/REC-html40/charset.html#h-5.3
    """
    value = SGML_CHARACTER_RE.sub(SGML_CHARACTER_REPL, value)
    value = SGML_SPACE_RE.sub(SGML_SPACE_REPL, value)
    return value

STYLE_COMMENT_RE = re.compile(r'\/\*[^*]*\*+([^/][^*]*\*+)*\/')
STYLE_COMMENT_REPL = ''

STYLE_CHARACTER_RE = re.compile(r'(?P<string>\\(?P<hex>[0-9a-fA-F]s{1,6})[ \t\r\n\f]?)')
def STYLE_CHARACTER_REPL(match):
    """Replace character entity with character"""
    dict = match.groupdict()
    try:
        code = int(dict['dec'])
        return unichr(code)
    except (ValueError, OverflowError):
        return dict['string']

def get_style(value):
    """
    Return unquoted style with removed comments.
    
    http://www.w3.org/TR/1998/REC-CSS2-19980512/syndata.html#q4
    """
    value = STYLE_COMMENT_RE.sub(STYLE_COMMENT_REPL, value)
#    value = STYLE_CHARACTER_RE.sub(STYLE_CHARACTER_REPL, value)
    return value

GET_LINED_SPACE_RE = re.compile('[\n\r\t]')
GET_LINED_SPACE_REPL = ' '

GET_LINED_NEW_LINE_RE = re.compile('(<[a-zA-Z]+)')
def GET_LINED_NEW_LINE_REPL(match):
    return '\n%s' % match.group(0)

def get_lined(value):
    """
    Return readable html, where each tag starts with new line. 
    """
    value = GET_LINED_SPACE_RE.sub(GET_LINED_SPACE_REPL, value)
    value = GET_LINED_NEW_LINE_RE.sub(GET_LINED_NEW_LINE_REPL, value)
    return value

def get_dict(source, leave=None, remove=None, append={}):
    """
    Return dictionary.
    
    ``source`` is source dictionary.
    
    ``leave`` is list with key`s names to be leaved.
    All other key will be removed.
    If ``leave`` is None than no items will be removed. 
    
    ``remove`` is list with key`s names to be removed.
    If ``remove`` is None than no items will be removed. 
    
    ``append`` is dictionary to update result dictionary.
    """
    result = {}
    for name, value in source.iteritems():
        if leave is not None and name not in leave:
            continue
        if remove is not None and name in remove:
            continue
        result[name] = value
    result.update(append)
    return result
