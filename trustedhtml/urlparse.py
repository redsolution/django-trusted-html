"""
http://www.ietf.org/rfc/rfc2396.txt
"""

import re

SPLIT_RE = re.compile(r'^(([^:/?#]+):)?(//([^/?#]*))?([^?#]*)(\?([^#]*))?(#(.*))?')

def split(url):
    """
    Split given ``url`` to the tuple
    (scheme, authority, path, query, fragment).
    """
    match = SPLIT_RE.match(url)
    return (match.group(2), match.group(4), match.group(5), match.group(7), match.group(9))

def expand(scheme, authority, path, query, fragment):
    """
    Expand url from given
    ``scheme``, ``authority``, ``path``, ``query``, ``fragment``.
    """
    result = u''
    if scheme is not None:
        result += scheme + ':'
    if authority is not None:
        result += '//' + authority
    if path is not None:
        result += path
    if query is not None:
        result += '?' + query
    if fragment is not None:
        result += '#' + fragment
    return result

FIX_QUOTES_RE = re.compile(r'%(?![0-9A-Fa-f]{2})')
FIX_QUOTES_RELP = '%25'

def fix(value):
    """
    Fix quotes in uri.
    """
    return FIX_QUOTES_RE.sub(FIX_QUOTES_RELP, value)
