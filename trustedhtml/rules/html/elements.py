"""
Index of Elements 
http://www.w3.org/TR/REC-html40/index/elements.html
"""

from trustedhtml.classes import Element

from trustedhtml.rules.html.attributes import attributes
from trustedhtml.rules.html.contents import contents

elements = {}

elements['a'] = Element(empty_element=True,
    rules=attributes['a'], contents=contents['a'])
# anchor

elements['abbr'] = Element(
    rules=attributes['abbr'], contents=contents['abbr'])
# abbreviated form (e.g., WWW, HTTP, etc.)

elements['acronym'] = Element(
    rules=attributes['acronym'], contents=contents['acronym'])
#

elements['address'] = Element(
    rules=attributes['address'], contents=contents['address'])
# information on author

elements['applet'] = Element(empty_element=True,
    rules=attributes['applet'], contents=contents['applet'])
# Java applet; Deprecated

elements['area'] = Element(
    rules=attributes['area'], contents=contents['area'])
# client-side image map area

elements['b'] = Element(
    rules=attributes['b'], contents=contents['b'])
# bold text style

elements['base'] = Element(
    rules=attributes['base'], contents=contents['base'])
# document base URI

elements['basefont'] = Element(
    rules=attributes['basefont'], contents=contents['basefont'])
# base font size; Deprecated

elements['bdo'] = Element(
    rules=attributes['bdo'], contents=contents['bdo'])
# I18N BiDi over-ride

elements['big'] = Element(
    rules=attributes['big'], contents=contents['big'])
# large text style

elements['blockquote'] = Element(
    rules=attributes['blockquote'], contents=contents['blockquote'])
# long quotation

elements['body'] = Element(empty_element=True, optional_start=True, optional_end=True,
    rules=attributes['body'], contents=contents['body'])
# document body

elements['br'] = Element(
    rules=attributes['br'], contents=contents['br'])
# forced line break

elements['button'] = Element(empty_element=True,
    rules=attributes['button'], contents=contents['button'])
# push button

elements['caption'] = Element(empty_element=True,
    rules=attributes['caption'], contents=contents['caption'])
# table caption

elements['center'] = Element(
    rules=attributes['center'], contents=contents['center'])
# shorthand for DIV align=center; Deprecated

elements['cite'] = Element(
    rules=attributes['cite'], contents=contents['cite'])
# citation

elements['code'] = Element(
    rules=attributes['code'], contents=contents['code'])
# computer code fragment

elements['col'] = Element(
    rules=attributes['col'], contents=contents['col'])
# table column

elements['colgroup'] = Element(optional_end=True,
    rules=attributes['colgroup'], contents=contents['colgroup'])
# table column group

elements['dd'] = Element(optional_end=True,
    rules=attributes['dd'], contents=contents['dd'])
# definition description

elements['del'] = Element(
    rules=attributes['del'], contents=contents['del'])
# deleted text

elements['dfn'] = Element(
    rules=attributes['dfn'], contents=contents['dfn'])
# instance definition

elements['dir'] = Element(
    rules=attributes['dir'], contents=contents['dir'])
# directory list; Deprecated

elements['div'] = Element(
    rules=attributes['div'], contents=contents['div'])
# generic language/style container

elements['dl'] = Element(
    rules=attributes['dl'], contents=contents['dl'])
# definition list

elements['dt'] = Element(optional_end=True,
    rules=attributes['dt'], contents=contents['dt'])
# definition term

elements['em'] = Element(
    rules=attributes['em'], contents=contents['em'])
# emphasis

elements['fieldset'] = Element(
    rules=attributes['fieldset'], contents=contents['fieldset'])
# form control group

elements['font'] = Element(
    rules=attributes['font'], contents=contents['font'])
# local change to font; Deprecated

elements['form'] = Element(
    rules=attributes['form'], contents=contents['form'])
# interactive form

elements['frame'] = Element(
    rules=attributes['frame'], contents=contents['frame'])
# subwindow

elements['frameset'] = Element(
    rules=attributes['frameset'], contents=contents['frameset'])
# window subdivision

elements['h1'] = Element(
    rules=attributes['h1'], contents=contents['h1'])
# heading

elements['h2'] = Element(
    rules=attributes['h2'], contents=contents['h2'])
# heading

elements['h3'] = Element(
    rules=attributes['h3'], contents=contents['h3'])
# heading

elements['h4'] = Element(
    rules=attributes['h4'], contents=contents['h4'])
# heading

elements['h5'] = Element(
    rules=attributes['h5'], contents=contents['h5'])
# heading

elements['h6'] = Element(
    rules=attributes['h6'], contents=contents['h6'])
# heading

elements['head'] = Element(optional_start=True, optional_end=True,
    rules=attributes['head'], contents=contents['head'])
# document head

elements['hr'] = Element(
    rules=attributes['hr'], contents=contents['hr'])
# horizontal rule

elements['html'] = Element(optional_start=True, optional_end=True,
    rules=attributes['html'], contents=contents['html'])
# document root element

elements['i'] = Element(
    rules=attributes['i'], contents=contents['i'])
# italic text style

elements['iframe'] = Element(empty_element=True,
    rules=attributes['iframe'], contents=contents['iframe'])
# inline subwindow

elements['img'] = Element(
    rules=attributes['img'], contents=contents['img'])
# Embedded image

elements['input'] = Element(
    rules=attributes['input'], contents=contents['input'])
# form control

elements['ins'] = Element(
    rules=attributes['ins'], contents=contents['ins'])
# inserted text

elements['isindex'] = Element(
    rules=attributes['isindex'], contents=contents['isindex'])
# single line prompt; Deprecated

elements['kbd'] = Element(
    rules=attributes['kbd'], contents=contents['kbd'])
# text to be entered by the user

elements['label'] = Element(
    rules=attributes['label'], contents=contents['label'])
# form field label text

elements['legend'] = Element(
    rules=attributes['legend'], contents=contents['legend'])
# fieldset legend

elements['li'] = Element(optional_end=True,
    rules=attributes['li'], contents=contents['li'])
# list item

elements['link'] = Element(
    rules=attributes['link'], contents=contents['link'])
# a media-independent link

elements['map'] = Element(
    rules=attributes['map'], contents=contents['map'])
# client-side image map

elements['menu'] = Element(
    rules=attributes['menu'], contents=contents['menu'])
# menu list; Deprecated

elements['meta'] = Element(
    rules=attributes['meta'], contents=contents['meta'])
# generic metainformation

elements['noframes'] = Element(
    rules=attributes['noframes'], contents=contents['noframes'])
# alternate content container for non frame-based rendering

elements['noscript'] = Element(
    rules=attributes['noscript'], contents=contents['noscript'])
# alternate content container for non script-based rendering

elements['object'] = Element(empty_element=True,
    rules=attributes['object'], contents=contents['object'])
# generic embedded object

elements['ol'] = Element(
    rules=attributes['ol'], contents=contents['ol'])
# ordered list

elements['optgroup'] = Element(empty_element=True,
    rules=attributes['optgroup'], contents=contents['optgroup'])
# option group

elements['option'] = Element(optional_end=True,
    rules=attributes['option'], contents=contents['option'])
# selectable choice

elements['p'] = Element(optional_end=True,
    rules=attributes['p'], contents=contents['p'])
# paragraph

elements['param'] = Element(
    rules=attributes['param'], contents=contents['param'])
# named property value

elements['pre'] = Element(
    rules=attributes['pre'], contents=contents['pre'])
# preformatted text

elements['q'] = Element(
    rules=attributes['q'], contents=contents['q'])
# short inline quotation

elements['s'] = Element(
    rules=attributes['s'], contents=contents['s'])
# strike-through text style; Deprecated

elements['samp'] = Element(
    rules=attributes['samp'], contents=contents['samp'])
# sample program output, scripts, etc.

elements['script'] = Element(remove_element=True, save_content=False,
    rules=attributes['script'], contents=contents['script'])
# script statements

elements['select'] = Element(
    rules=attributes['select'], contents=contents['select'])
# option selector

elements['small'] = Element(
    rules=attributes['small'], contents=contents['small'])
# small text style

elements['span'] = Element(
    rules=attributes['span'], contents=contents['span'])
# generic language/style container

elements['strike'] = Element(
    rules=attributes['strike'], contents=contents['strike'])
# strike-through text; Deprecated

elements['strong'] = Element(
    rules=attributes['strong'], contents=contents['strong'])
# strong emphasis

elements['style'] = Element(remove_element=True, save_content=False,
    rules=attributes['style'], contents=contents['style'])
# style info

elements['sub'] = Element(
    rules=attributes['sub'], contents=contents['sub'])
# subscript

elements['sup'] = Element(
    rules=attributes['sup'], contents=contents['sup'])
# superscript

elements['table'] = Element(
    rules=attributes['table'], contents=contents['table'])
#

elements['tbody'] = Element(optional_start=True, optional_end=True,
    rules=attributes['tbody'], contents=contents['tbody'])
# table body

elements['td'] = Element(default='&nbsp;', optional_end=True,
    rules=attributes['td'], contents=contents['td'])
# table data cell

elements['textarea'] = Element(empty_element=True,
    rules=attributes['textarea'], contents=contents['textarea'])
# multi-line text field

elements['tfoot'] = Element(optional_end=True,
    rules=attributes['tfoot'], contents=contents['tfoot'])
# table footer

elements['th'] = Element(default='&nbsp;', optional_end=True,
    rules=attributes['th'], contents=contents['th'])
# table header cell

elements['thead'] = Element(optional_end=True,
    rules=attributes['thead'], contents=contents['thead'])
# table header

elements['title'] = Element(
    rules=attributes['title'], contents=contents['title'])
# document title

elements['tr'] = Element(optional_end=True,
    rules=attributes['tr'], contents=contents['tr'])
# table row

elements['tt'] = Element(
    rules=attributes['tt'], contents=contents['tt'])
# teletype or monospaced text style

elements['u'] = Element(
    rules=attributes['u'], contents=contents['u'])
# underlined text style; Deprecated

elements['ul'] = Element(
    rules=attributes['ul'], contents=contents['ul'])
# unordered list

elements['var'] = Element(
    rules=attributes['var'], contents=contents['var'])
# instance of a variable or program argument

elements['noindex'] = Element(
    rules=attributes['noindex'], contents=contents['noindex'])
# This not w3c tag, but it is used by Yandex search engine
