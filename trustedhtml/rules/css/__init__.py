"""
``values`` dictionary contains all specified css rules.  
"""
import consts
import grammar
import syndata
import box
import visuren
import visudet
import visufx
import generate
import page
import colors
import fonts
import text
import tables
import ui
import values
import custom

from trustedhtml.classes import Style

full = Style(allow_empty=False, rules=values.values)
common = Style(allow_empty=False, rules=custom.common)
tables = Style(allow_empty=False, rules=custom.tables)
images = Style(allow_empty=False, rules=custom.images)
#    allowed_value=List(values='inherit'),
