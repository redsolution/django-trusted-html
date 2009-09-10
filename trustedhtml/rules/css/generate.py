"""
Generated content, automatic numbering, and lists
http://www.w3.org/TR/1998/REC-CSS2-19980512/generate.html
"""

from trustedhtml.classes import List, RegExp, No, Or, Sequence, Complex

from trustedhtml.rules.css.consts import inherit, none, auto
from trustedhtml.rules.css.grammar import grammar
from trustedhtml.rules.css.syndata import length, string, uri_image

content = No()
# Applies to: :before and :after pseudo-elements

quotes = Or(rules=[
    Sequence(rule=string, min_split=1), none, inherit,
])
# Bug: strings must be in pairs

identifier_and_integer = RegExp(
    regexp=r'(%(w)s(?P<a>%(ident)s)%(w)s(?P<b>%(int)s)+%(w)s)$' % grammar,
    expand=r'\g<a> \g<b>)',
)

counter_reset = Or(rules=[
    Sequence(rule=identifier_and_integer, min_split=1), none, inherit,
])

marker_offset = Or(rules=[
    length, auto, inherit,
])

list_style_type = List(values=[
    'disc', 'circle', 'square', 'decimal', 'decimal-leading-zero', 
    'lower-roman', 'upper-roman', 'lower-greek', 'lower-alpha', 
    'lower-latin', 'upper-alpha', 'upper-latin', 'hebrew', 
    'armenian', 'georgian', 'cjk-ideographic', 'hiragana', 
    'katakana', 'hiragana-iroha', 'katakana-iroha', 'none',
    'inherit',
])
# Applies to: elements with 'display: list-item'  

list_style_image = Or(rules=[
    uri_image, none, inherit
])
# Applies to: elements with 'display: list-item'  

list_style_position = List(values=[
    'inside', 'outside',
    'inherit',
])
# Applies to: elements with 'display: list-item'  

list_style = Or(rules=[
    Complex(rules=[
        list_style_type,
        list_style_position,
        list_style_image,
    ]), inherit,
])
# Applies to: elements with 'display: list-item'  
