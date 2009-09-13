"""
Index of Elements 
http://www.w3.org/TR/REC-html40/index/elements.html
"""

from trustedhtml.classes import Element

from trustedhtml.rules.html.attributes import attributes

elements = {}

elements['a'] = Element(allow_empty=True, rules=attributes['a'])
# anchor

elements['abbr'] = Element(rules=attributes['abbr'])
# abbreviated form (e.g., WWW, HTTP, etc.)

elements['acronym'] = Element(rules=attributes['acronym'])
# 

elements['address'] = Element(rules=attributes['address'])
# information on author

elements['applet'] = Element(allow_empty=True, rules=attributes['applet'])
# Java applet; Deprecated

elements['area'] = Element(empty_tag=True, rules=attributes['area'])
# client-side image map area

elements['b'] = Element(rules=attributes['b'])
# bold text style

elements['base'] = Element(empty_tag=True, rules=attributes['base'])
# document base URI

elements['basefont'] = Element(empty_tag=True, rules=attributes['basefont'])
# base font size; Deprecated

elements['bdo'] = Element(rules=attributes['bdo'])
# I18N BiDi over-ride

elements['big'] = Element(rules=attributes['big'])
# large text style

elements['blockquote'] = Element(rules=attributes['blockquote'])
# long quotation

elements['body'] = Element(allow_empty=True, optional_start=True, optional_end=True, rules=attributes['body'])
# document body

elements['br'] = Element(empty_tag=True, rules=attributes['br'])
# forced line break

elements['button'] = Element(allow_empty=True, rules=attributes['button'])
# push button

elements['caption'] = Element(allow_empty=True, rules=attributes['caption'])
# table caption

elements['center'] = Element(rules=attributes['center'])
# shorthand for DIV align=center; Deprecated

elements['cite'] = Element(rules=attributes['cite'])
# citation

elements['code'] = Element(rules=attributes['code'])
# computer code fragment

elements['col'] = Element(empty_tag=True, rules=attributes['col'])
# table column

elements['colgroup'] = Element(optional_end=True, rules=attributes['colgroup'])
# table column group

elements['dd'] = Element(optional_end=True, rules=attributes['dd'])
# definition description

elements['del'] = Element(rules=attributes['del'])
# deleted text

elements['dfn'] = Element(rules=attributes['dfn'])
# instance definition

elements['dir'] = Element(rules=attributes['dir'])
# directory list; Deprecated

elements['div'] = Element(rules=attributes['div'])
# generic language/style container

elements['dl'] = Element(rules=attributes['dl'])
# definition list

elements['dt'] = Element(optional_end=True, rules=attributes['dt'])
# definition term

elements['em'] = Element(rules=attributes['em'])
# emphasis

elements['fieldset'] = Element(rules=attributes['fieldset'])
# form control group

elements['font'] = Element(rules=attributes['font'])
# local change to font; Deprecated

elements['form'] = Element(rules=attributes['form'])
# interactive form

elements['frame'] = Element(empty_tag=True, rules=attributes['frame'])
# subwindow

elements['frameset'] = Element(rules=attributes['frameset'])
# window subdivision

elements['h1'] = Element(rules=attributes['h1'])
# heading

elements['h2'] = Element(rules=attributes['h2'])
# heading

elements['h3'] = Element(rules=attributes['h3'])
# heading

elements['h4'] = Element(rules=attributes['h4'])
# heading

elements['h5'] = Element(rules=attributes['h5'])
# heading

elements['h6'] = Element(rules=attributes['h6'])
# heading

elements['head'] = Element(optional_start=True, optional_end=True, rules=attributes['head'])
# document head

elements['hr'] = Element(empty_tag=True, rules=attributes['hr'])
# horizontal rule

elements['html'] = Element(optional_start=True, optional_end=True, rules=attributes['html'])
# document root element

elements['i'] = Element(rules=attributes['i'])
# italic text style

elements['iframe'] = Element(allow_empty=True, rules=attributes['iframe'])
# inline subwindow

elements['img'] = Element(empty_tag=True, rules=attributes['img'])
# Embedded image

elements['input'] = Element(empty_tag=True, rules=attributes['input'])
# form control

elements['ins'] = Element(rules=attributes['ins'])
# inserted text

elements['isindex'] = Element(empty_tag=True, rules=attributes['isindex'])
# single line prompt; Deprecated

elements['kbd'] = Element(rules=attributes['kbd'])
# text to be entered by the user

elements['label'] = Element(rules=attributes['label'])
# form field label text

elements['legend'] = Element(rules=attributes['legend'])
# fieldset legend

elements['li'] = Element(optional_end=True, rules=attributes['li'])
# list item

elements['link'] = Element(empty_tag=True, rules=attributes['link'])
# a media-independent link

elements['map'] = Element(rules=attributes['map'])
# client-side image map

elements['menu'] = Element(rules=attributes['menu'])
# menu list; Deprecated

elements['meta'] = Element(empty_tag=True, rules=attributes['meta'])
# generic metainformation

elements['noframes'] = Element(rules=attributes['noframes'])
# alternate content container for non frame-based rendering

elements['noscript'] = Element(rules=attributes['noscript'])
# alternate content container for non script-based rendering

elements['object'] = Element(allow_empty=True, rules=attributes['object'])
# generic embedded object

elements['ol'] = Element(rules=attributes['ol'])
# ordered list

elements['optgroup'] = Element(allow_empty=True, rules=attributes['optgroup'])
# option group

elements['option'] = Element(optional_end=True, rules=attributes['option'])
# selectable choice

elements['p'] = Element(optional_end=True, rules=attributes['p'])
# paragraph

elements['param'] = Element(empty_tag=True, rules=attributes['param'])
# named property value

elements['pre'] = Element(rules=attributes['pre'])
# preformatted text

elements['q'] = Element(rules=attributes['q'])
# short inline quotation

elements['s'] = Element(rules=attributes['s'])
# strike-through text style; Deprecated

elements['samp'] = Element(rules=attributes['samp'])
# sample program output, scripts, etc.

elements['script'] = Element(rules=attributes['script'])
# script statements

elements['select'] = Element(rules=attributes['select'])
# option selector

elements['small'] = Element(rules=attributes['small'])
# small text style

elements['span'] = Element(rules=attributes['span'])
# generic language/style container

elements['strike'] = Element(rules=attributes['strike'])
# strike-through text; Deprecated

elements['strong'] = Element(rules=attributes['strong'])
# strong emphasis

elements['style'] = Element(rules=attributes['style'])
# style info

elements['sub'] = Element(rules=attributes['sub'])
# subscript

elements['sup'] = Element(rules=attributes['sup'])
# superscript

elements['table'] = Element(rules=attributes['table'])
# 

elements['tbody'] = Element(optional_start=True, optional_end=True, rules=attributes['tbody'])
# table body

elements['td'] = Element(default='&nbsp;', optional_end=True, rules=attributes['td'])
# table data cell

elements['textarea'] = Element(allow_empty=True, rules=attributes['textarea'])
# multi-line text field

elements['tfoot'] = Element(optional_end=True, rules=attributes['tfoot'])
# table footer

elements['th'] = Element(default='&nbsp;', optional_end=True, rules=attributes['th'])
# table header cell

elements['thead'] = Element(optional_end=True, rules=attributes['thead'])
# table header

elements['title'] = Element(rules=attributes['title'])
# document title

elements['tr'] = Element(optional_end=True, rules=attributes['tr'])
# table row

elements['tt'] = Element(rules=attributes['tt'])
# teletype or monospaced text style

elements['u'] = Element(rules=attributes['u'])
# underlined text style; Deprecated

elements['ul'] = Element(rules=attributes['ul'])
# unordered list

elements['var'] = Element(rules=attributes['var'])
# instance of a variable or program argument
