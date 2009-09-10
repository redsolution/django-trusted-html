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

from trustedhtml.classes import Style

full = Style(rules=values.values)
#    allowed_value=List(values='inherit'),
