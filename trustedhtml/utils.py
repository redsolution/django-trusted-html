"""Utils used by classes"""

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
    'agrave': 192,
    'aacute': 193,
    'acirc': 194,
    'atilde': 195,
    'auml': 196,
    'aring': 197,
    'aelig': 198,
    'ccedil': 199,
    'egrave': 200,
    'eacute': 201,
    'ecirc': 202,
    'euml': 203,
    'igrave': 204,
    'iacute': 205,
    'icirc': 206,
    'iuml': 207,
    'eth': 208,
    'ntilde': 209,
    'ograve': 210,
    'oacute': 211,
    'ocirc': 212,
    'otilde': 213,
    'ouml': 214,
    'times': 215,
    'oslash': 216,
    'ugrave': 217,
    'uacute': 218,
    'ucirc': 219,
    'uuml': 220,
    'yacute': 221,
    'thorn': 222,
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
    # latin extended-b
    'fnof': 402,
    # c0 controls and basic latin
    'quot': 34,
    'amp': 38,
    'lt': 60,
    'gt': 62,
    # latin extended-a
    'oelig': 338,
    'oelig': 339,
    'scaron': 352,
    'scaron': 353,
    'yuml': 376,
    # spacing modifier letters
    'circ': 710,
    'tilde': 732,
    # general punctuation
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
    'dagger': 8225,
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
    # general punctuation
    'bull': 8226,
    'hellip': 8230,
    'prime': 8242,
    'prime': 8243,
    'oline': 8254,
    'frasl': 8260,
    # letterlike symbols
    'weierp': 8472,
    'image': 8465,
    'real': 8476,
    'trade': 8482,
    'alefsym': 8501,
    # arrows
    'larr': 8592,
    'uarr': 8593,
    'rarr': 8594,
    'darr': 8595,
    'harr': 8596,
    'crarr': 8629,
    'larr': 8656,
    'uarr': 8657,
    'rarr': 8658,
    'darr': 8659,
    'harr': 8660,
    # mathematical operators
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
    # miscellaneous technical
    'lceil': 8968,
    'rceil': 8969,
    'lfloor': 8970,
    'rfloor': 8971,
    'lang': 9001,
    'rang': 9002,
    # geometric shapes
    'loz': 9674,
    # miscellaneous symbols
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
            code = CHARACTER_ENTITIES[dict['name'].lower()]
        else:
            raise ValueError
        return unichr(code)
    except (ValueError, IndexError, OverflowError):
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

URI_PERCENT_RE = re.compile(r'%(?![0-9A-Fa-f]{2})')
URI_PERCENT_RELP = '%25'

def get_uri(value):
    """
    Return unquoted URI.
    
    http://www.ietf.org/rfc/rfc2396.txt
    """
    return URI_PERCENT_RE.sub(URI_PERCENT_RELP, value)

STYLE_COMMENT_RE = re.compile(r'\/\*[^*]*\*+([^/][^*]*\*+)*\/')
STYLE_COMMENT_REPL = ''

STYLE_CHARACTER_RE = re.compile(r'(?P<string>\\(?P<hex>[0-9a-f]s{1,6})[ \t\r\n\f]?)')
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
