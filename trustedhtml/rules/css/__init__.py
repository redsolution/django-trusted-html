import values
import custom

from trustedhtml.classes import Style

full = Style(rules=values.values)
common = Style(rules=custom.common)
tables = Style(rules=custom.tables)
images = Style(rules=custom.images)
# Fix: allowed_value=List(values='inherit'),
