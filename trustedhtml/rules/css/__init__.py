"""
``index`` dictionary contains all specified css rules.  
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

index = {}
index['margin-top'] = index['margin-right'] = index['margin-bottom'] = index['margin-left'] = box.margin_top
index['margin'] = box.margin
index['padding-top'] = index['padding-right'] = index['padding-bottom'] = index['padding-left'] = box.padding_top
index['padding'] = box.padding
index['border-top-width'] = index['border-right-width'] = index['border-bottom-width'] = index['border-left-width'] = box.border_top_width
index['border-width'] = box.border_width
index['border-top-color'] = index['border-right-color'] = index['border-bottom-color'] = index['border-left-color'] = box.border_top_color
index['border-color'] = box.border_color
index['border-top-style'] = index['border-right-style'] = index['border-bottom-style'] = index['border-left-style'] = box.border_top_style
index['border-style'] = box.border_style
index['border-top'] = index['border-right'] = index['border-bottom'] = index['border-left'] = index['border'] = box.border

index['display'] = visuren.display
index['position'] = visuren.position
index['top'] = index['right'] = index['bottom'] = index['left'] = visuren.top
index['float'] = visuren.float
index['clear'] = visuren.clear
index['z-index'] = visuren.z_index
index['direction'] = visuren.direction
index['unicode-bidi'] = visuren.unicode_bidi

index['width'] = index['height'] = visudet.width
index['min-width'] = index['min-height'] = visudet.min_width
index['max-width'] = index['max-height'] = visudet.max_width
index['line-height'] = visudet.line_height
index['vertical-align'] = visudet.vertical_align

index['overflow'] = visufx.overflow
index['clip'] = visufx.clip
index['visibility'] = visufx.visibility

index['content'] = generate.content
index['quotes'] = generate.quotes
index['counter-reset'] = index['counter-increment'] = generate.counter_reset
index['marker-offset'] = generate.marker_offset
index['list-style-type'] = generate.list_style_type
index['list-style-image'] = generate.list_style_image
index['list-style-position'] = generate.list_style_position
index['list-style'] = generate.list_style

index['size'] = page.size
index['marks'] = page.marks
index['page-break-before'] = index['page-break-after'] = page.page_break_before
index['page-break-inside'] = page.page_break_inside
index['page'] = page.page
index['orphans'] = index['widows'] = page.orphans

index['color'] = colors.color
index['background-color'] = colors.background_color
index['background-image'] = colors.background_image
index['background-repeat'] = colors.background_repeat
index['background-attachment'] = colors.background_attachment
index['background-position'] = colors.background_position
index['background'] = colors.background

index['font-family'] = fonts.font_family
index['font-style'] = fonts.font_style
index['font-variant'] = fonts.font_variant
index['font-weight'] = fonts.font_weight
index['font-stretch'] = fonts.font_stretch
index['font-size'] = fonts.font_size
index['font-size-adjust'] = fonts.font_size_adjust
index['font'] = fonts.font

index['text-indent'] = text.text_indent
index['text-align'] = text.text_align
index['text-decoration'] = text.text_decoration
index['text-shadow'] = text.text_shadow
index['letter-spacing'] = index['word-spacing'] = text.letter_spacing
index['text-transform'] = text.text_transform
index['white-space'] = text.white_space

index['caption-side'] = tables.caption_side
index['table-layout'] = tables.table_layout
index['border-collapse'] = tables.border_collapse
index['border-spacing'] = tables.border_spacing
index['empty-cells'] = tables.empty_cells
index['speak-header'] = tables.speak_header

index['cursor'] = ui.cursor
index['outline-width'] = ui.outline_width
index['outline-style'] = ui.outline_style
index['outline-color'] = ui.outline_color
index['outline'] = ui.outline
