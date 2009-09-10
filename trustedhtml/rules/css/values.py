"""
``values`` dictionary contains all specified css rules.  
"""
from trustedhtml.rules.css import consts
from trustedhtml.rules.css import grammar
from trustedhtml.rules.css import syndata
from trustedhtml.rules.css import box
from trustedhtml.rules.css import visuren
from trustedhtml.rules.css import visudet
from trustedhtml.rules.css import visufx
from trustedhtml.rules.css import generate
from trustedhtml.rules.css import page
from trustedhtml.rules.css import colors
from trustedhtml.rules.css import fonts
from trustedhtml.rules.css import text
from trustedhtml.rules.css import tables
from trustedhtml.rules.css import ui

values = {}
values['margin-top'] = values['margin-right'] = values['margin-bottom'] = values['margin-left'] = box.margin_top
values['margin'] = box.margin
values['padding-top'] = values['padding-right'] = values['padding-bottom'] = values['padding-left'] = box.padding_top
values['padding'] = box.padding
values['border-top-width'] = values['border-right-width'] = values['border-bottom-width'] = values['border-left-width'] = box.border_top_width
values['border-width'] = box.border_width
values['border-top-color'] = values['border-right-color'] = values['border-bottom-color'] = values['border-left-color'] = box.border_top_color
values['border-color'] = box.border_color
values['border-top-style'] = values['border-right-style'] = values['border-bottom-style'] = values['border-left-style'] = box.border_top_style
values['border-style'] = box.border_style
values['border-top'] = values['border-right'] = values['border-bottom'] = values['border-left'] = values['border'] = box.border

values['display'] = visuren.display
values['position'] = visuren.position
values['top'] = values['right'] = values['bottom'] = values['left'] = visuren.top
values['float'] = visuren.float
values['clear'] = visuren.clear
values['z-index'] = visuren.z_index
values['direction'] = visuren.direction
values['unicode-bidi'] = visuren.unicode_bidi

values['width'] = values['height'] = visudet.width
values['min-width'] = values['min-height'] = visudet.min_width
values['max-width'] = values['max-height'] = visudet.max_width
values['line-height'] = visudet.line_height
values['vertical-align'] = visudet.vertical_align

values['overflow'] = visufx.overflow
values['clip'] = visufx.clip
values['visibility'] = visufx.visibility

values['content'] = generate.content
values['quotes'] = generate.quotes
values['counter-reset'] = values['counter-increment'] = generate.counter_reset
values['marker-offset'] = generate.marker_offset
values['list-style-type'] = generate.list_style_type
values['list-style-image'] = generate.list_style_image
values['list-style-position'] = generate.list_style_position
values['list-style'] = generate.list_style

values['size'] = page.size
values['marks'] = page.marks
values['page-break-before'] = values['page-break-after'] = page.page_break_before
values['page-break-inside'] = page.page_break_inside
values['page'] = page.page
values['orphans'] = values['widows'] = page.orphans

values['color'] = colors.color
values['background-color'] = colors.background_color
values['background-image'] = colors.background_image
values['background-repeat'] = colors.background_repeat
values['background-attachment'] = colors.background_attachment
values['background-position'] = colors.background_position
values['background'] = colors.background

values['font-family'] = fonts.font_family
values['font-style'] = fonts.font_style
values['font-variant'] = fonts.font_variant
values['font-weight'] = fonts.font_weight
values['font-stretch'] = fonts.font_stretch
values['font-size'] = fonts.font_size
values['font-size-adjust'] = fonts.font_size_adjust
values['font'] = fonts.font

values['text-indent'] = text.text_indent
values['text-align'] = text.text_align
values['text-decoration'] = text.text_decoration
values['text-shadow'] = text.text_shadow
values['letter-spacing'] = values['word-spacing'] = text.letter_spacing
values['text-transform'] = text.text_transform
values['white-space'] = text.white_space

values['caption-side'] = tables.caption_side
values['table-layout'] = tables.table_layout
values['border-collapse'] = tables.border_collapse
values['border-spacing'] = tables.border_spacing
values['empty-cells'] = tables.empty_cells
values['speak-header'] = tables.speak_header

values['cursor'] = ui.cursor
values['outline-width'] = ui.outline_width
values['outline-style'] = ui.outline_style
values['outline-color'] = ui.outline_color
values['outline'] = ui.outline
