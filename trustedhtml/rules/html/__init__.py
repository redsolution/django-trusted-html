import elements
import custom

from trustedhtml.classes import Html

full = Html(rules=elements.elements, root_tags=contents.contents['body'])
pretty = Html(rules=custom.pretty, root_tags=contents.contents['body'])
normal = Html(rules=custom.normal, root_tags=contents.contents['body'])
