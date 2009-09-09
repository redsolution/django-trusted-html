"""
Index of Elements 
http://www.w3.org/TR/REC-html40/index/elements.html
"""

elements = {}

elements['a'] = Element()
# anchor

elements['abbr'] = Element()
# abbreviated form (e.g., WWW, HTTP, etc.)

elements['acronym'] = Element()
# 

elements['address'] = Element()
# information on author

elements['applet'] = Element(deprecated=True, )
# Java applet

elements['area'] = Element(empty=True, )
# client-side image map area

elements['b'] = Element()
# bold text style

elements['base'] = Element(empty=True, )
# document base URI

elements['basefont'] = Element(empty=True, deprecated=True, )
# base font size

elements['bdo'] = Element()
# I18N BiDi over-ride

elements['big'] = Element()
# large text style

elements['blockquote'] = Element()
# long quotation

elements['body'] = Element(optional_start=True, optional_end=True, )
# document body

elements['br'] = Element(empty=True, )
# forced line break

elements['button'] = Element()
# push button

elements['caption'] = Element()
# table caption

elements['center'] = Element(deprecated=True, )
# shorthand for DIV align=center

elements['cite'] = Element()
# citation

elements['code'] = Element()
# computer code fragment

elements['col'] = Element(empty=True, )
# table column

elements['colgroup'] = Element(optional_end=True, )
# table column group

elements['dd'] = Element(optional_end=True, )
# definition description

elements['del'] = Element()
# deleted text

elements['dfn'] = Element()
# instance definition

elements['dir'] = Element(deprecated=True, )
# directory list

elements['div'] = Element()
# generic language/style container

elements['dl'] = Element()
# definition list

elements['dt'] = Element(optional_end=True, )
# definition term

elements['em'] = Element()
# emphasis

elements['fieldset'] = Element()
# form control group

elements['font'] = Element(deprecated=True, )
# local change to font

elements['form'] = Element()
# interactive form

elements['frame'] = Element(empty=True, )
# subwindow, Frameset DTD, 

elements['frameset'] = Element()
# window subdivision, Frameset DTD, 

elements['h1'] = Element()
# heading

elements['h2'] = Element()
# heading

elements['h3'] = Element()
# heading

elements['h4'] = Element()
# heading

elements['h5'] = Element()
# heading

elements['h6'] = Element()
# heading

elements['head'] = Element(optional_start=True, optional_end=True, )
# document head

elements['hr'] = Element(empty=True, )
# horizontal rule

elements['html'] = Element(optional_start=True, optional_end=True, )
# document root element

elements['i'] = Element()
# italic text style

elements['iframe'] = Element()
# inline subwindow

elements['img'] = Element(empty=True, )
# Embedded image

elements['input'] = Element(empty=True, )
# form control

elements['ins'] = Element()
# inserted text

elements['isindex'] = Element(empty=True, deprecated=True, )
# single line prompt

elements['kbd'] = Element()
# text to be entered by the user

elements['label'] = Element()
# form field label text

elements['legend'] = Element()
# fieldset legend

elements['li'] = Element(optional_end=True, )
# list item

elements['link'] = Element(empty=True, )
# a media-independent link

elements['map'] = Element()
# client-side image map

elements['menu'] = Element(deprecated=True, )
# menu list

elements['meta'] = Element(empty=True, )
# generic metainformation

elements['noframes'] = Element()
# alternate content container for non frame-based rendering, Frameset DTD, 

elements['noscript'] = Element()
# alternate content container for non script-based rendering

elements['object'] = Element()
# generic embedded object

elements['ol'] = Element()
# ordered list

elements['optgroup'] = Element()
# option group

elements['option'] = Element(optional_end=True, )
# selectable choice

elements['p'] = Element(optional_end=True, )
# paragraph

elements['param'] = Element(empty=True, )
# named property value

elements['pre'] = Element()
# preformatted text

elements['q'] = Element()
# short inline quotation

elements['s'] = Element(deprecated=True, )
# strike-through text style

elements['samp'] = Element()
# sample program output, scripts, etc.

elements['script'] = Element()
# script statements

elements['select'] = Element()
# option selector

elements['small'] = Element()
# small text style

elements['span'] = Element()
# generic language/style container

elements['strike'] = Element(deprecated=True, )
# strike-through text

elements['strong'] = Element()
# strong emphasis

elements['style'] = Element()
# style info

elements['sub'] = Element()
# subscript

elements['sup'] = Element()
# superscript

elements['table'] = Element()
# 

elements['tbody'] = Element(optional_start=True, optional_end=True, )
# table body

elements['td'] = Element(optional_end=True, )
# table data cell

elements['textarea'] = Element()
# multi-line text field

elements['tfoot'] = Element(optional_end=True, )
# table footer

elements['th'] = Element(optional_end=True, )
# table header cell

elements['thead'] = Element(optional_end=True, )
# table header

elements['title'] = Element()
# document title

elements['tr'] = Element(optional_end=True, )
# table row

elements['tt'] = Element()
# teletype or monospaced text style

elements['u'] = Element(deprecated=True, )
# underlined text style

elements['ul'] = Element()
# unordered list

elements['var'] = Element()
# instance of a variable or program argument
