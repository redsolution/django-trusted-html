"""
Index of Elements 
http://www.w3.org/TR/REC-html40/index/elements.html
"""

#Element.OPTIONAL
#Element.FORBIDDEN

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
# Java applet, Loose DTD

elements['area'] = Element(end=Element.FORBIDDEN, empty=True, )
# client-side image map area

elements['b'] = Element()
# bold text style

elements['base'] = Element(end=Element.FORBIDDEN, empty=True, )
# document base URI

elements['basefont'] = Element(end=Element.FORBIDDEN, empty=True, deprecated=True, )
# base font size, Loose DTD

elements['bdo'] = Element()
# I18N BiDi over-ride

elements['big'] = Element()
# large text style

elements['blockquote'] = Element()
# long quotation

elements['body'] = Element(start=Element.OPTIONAL, end=Element.OPTIONAL, )
# document body

elements['br'] = Element(end=Element.FORBIDDEN, empty=True, )
# forced line break

elements['button'] = Element()
# push button

elements['caption'] = Element()
# table caption

elements['center'] = Element(deprecated=True, )
# shorthand for DIV align=center, Loose DTD

elements['cite'] = Element()
# citation

elements['code'] = Element()
# computer code fragment

elements['col'] = Element(end=Element.FORBIDDEN, empty=True, )
# table column

elements['colgroup'] = Element(end=Element.OPTIONAL, )
# table column group

elements['dd'] = Element(end=Element.OPTIONAL, )
# definition description

elements['del'] = Element()
# deleted text

elements['dfn'] = Element()
# instance definition

elements['dir'] = Element(deprecated=True, )
# directory list, Loose DTD

elements['div'] = Element()
# generic language/style container

elements['dl'] = Element()
# definition list

elements['dt'] = Element(end=Element.OPTIONAL, )
# definition term

elements['em'] = Element()
# emphasis

elements['fieldset'] = Element()
# form control group

elements['font'] = Element(deprecated=True, )
# local change to font, Loose DTD

elements['form'] = Element()
# interactive form

elements['frame'] = Element(end=Element.FORBIDDEN, empty=True, )
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

elements['head'] = Element(start=Element.OPTIONAL, end=Element.OPTIONAL, )
# document head

elements['hr'] = Element(end=Element.FORBIDDEN, empty=True, )
# horizontal rule

elements['html'] = Element(start=Element.OPTIONAL, end=Element.OPTIONAL, )
# document root element

elements['i'] = Element()
# italic text style

elements['iframe'] = Element()
# inline subwindow, Loose DTD

elements['img'] = Element(end=Element.FORBIDDEN, empty=True, )
# Embedded image

elements['input'] = Element(end=Element.FORBIDDEN, empty=True, )
# form control

elements['ins'] = Element()
# inserted text

elements['isindex'] = Element(end=Element.FORBIDDEN, empty=True, deprecated=True, )
# single line prompt, Loose DTD

elements['kbd'] = Element()
# text to be entered by the user

elements['label'] = Element()
# form field label text

elements['legend'] = Element()
# fieldset legend

elements['li'] = Element(end=Element.OPTIONAL, )
# list item

elements['link'] = Element(end=Element.FORBIDDEN, empty=True, )
# a media-independent link

elements['map'] = Element()
# client-side image map

elements['menu'] = Element(deprecated=True, )
# menu list, Loose DTD

elements['meta'] = Element(end=Element.FORBIDDEN, empty=True, )
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

elements['option'] = Element(end=Element.OPTIONAL, )
# selectable choice

elements['p'] = Element(end=Element.OPTIONAL, )
# paragraph

elements['param'] = Element(end=Element.FORBIDDEN, empty=True, )
# named property value

elements['pre'] = Element()
# preformatted text

elements['q'] = Element()
# short inline quotation

elements['s'] = Element(deprecated=True, )
# strike-through text style, Loose DTD

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
# strike-through text, Loose DTD

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

elements['tbody'] = Element(start=Element.OPTIONAL, end=Element.OPTIONAL, )
# table body

elements['td'] = Element(end=Element.OPTIONAL, )
# table data cell

elements['textarea'] = Element()
# multi-line text field

elements['tfoot'] = Element(end=Element.OPTIONAL, )
# table footer

elements['th'] = Element(end=Element.OPTIONAL, )
# table header cell

elements['thead'] = Element(end=Element.OPTIONAL, )
# table header

elements['title'] = Element()
# document title

elements['tr'] = Element(end=Element.OPTIONAL, )
# table row

elements['tt'] = Element()
# teletype or monospaced text style

elements['u'] = Element(deprecated=True, )
# underlined text style, Loose DTD

elements['ul'] = Element()
# unordered list

elements['var'] = Element()
# instance of a variable or program argument

