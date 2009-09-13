"""
"""
import grammar
import types
import values
import attributes
import contents
import elements
import custom

from trustedhtml.classes import Html

full = Html(rules=elements.elements, root_tags=contents.contents['body'])
simple = Html(rules=custom.simple, root_tags=contents.contents['body'])
normal = Html(rules=custom.normal, root_tags=contents.contents['body'])
