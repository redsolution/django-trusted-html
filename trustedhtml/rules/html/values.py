"""
Values for Index of Attributes
http://www.w3.org/TR/REC-html40/index/attributes.html

Attributes for different elements can have different validation mechanism.
In such case we will use different names:
name of attribute followed immediately by an '~' character followed immediately
by [a-z] character.

Attributes for different elements can have same validation mechanism,
but separated in specification because of meaning.
In such case we will assign same values to the same attributes.
We do it to parse descriptions and generate ``map.py``.
"""

from trustedhtml.classes import RegExp, Sequence

from trustedhtml.rules.html.types import name, name_required, idrefs, \
    idrefs_comma, number, number_required, positive_number, text, \
    text_required, text_default, uri, uri_required, uri_image, uri_object, \
    uri_image_required, uris, color, pixels, length, multi_length, \
    multi_lengths, length_required, coords, content_type, content_types, \
    content_type_required, language_code, charset, charsets, character, \
    datetime, link_types, media_descs, style_sheet, frame_target, script

values = {}

values['abbr'] = text
# abbreviation for header cell (TD, TH)

values['accept-charset'] = charsets
# list of supported charsets (FORM)

values['accept'] = content_types
# list of MIME types for file upload (FORM, INPUT)

values['accesskey'] = character
# accessibility key character (A, AREA, BUTTON, INPUT, LABEL, LEGEND, TEXTAREA)

values['action'] = uri_required
# server-side form handler (FORM)

values['align~c'] = RegExp(regexp=r'(top|bottom|left|right)$')
# relative to table (CAPTION); deprecated

values['align~i'] = RegExp(regexp=r'(top|middle|bottom|left|right)$')
# vertical or horizontal alignment (APPLET, IFRAME, IMG, INPUT, OBJECT); deprecated

values['align~l'] = RegExp(regexp=r'(top|bottom|left|right)$')
# relative to fieldset (LEGEND); deprecated

values['align~t'] = RegExp(regexp=r'(left|center|right)$')
# table position relative to window (TABLE); deprecated

values['align~h'] = RegExp(regexp=r'(left|center|right)$')
# (HR); deprecated

values['align~d'] = RegExp(regexp=r'(left|center|right|justify)$')
# align, text alignment (DIV, H1, H2, H3, H4, H5, H6, P); deprecated

values['align'] = RegExp(regexp=r'(left|center|right|justify|char)$')
# (COL, COLGROUP, TBODY, TD, TFOOT, TH, THEAD, TR)

values['alink'] = color
# color of selected links (BODY); deprecated

values['alt'] = text
# short description (APPLET); deprecated

values['alt~r'] = text_required
# short description (AREA, IMG)

values['alt~i'] = text_default
# Fix for IMG, that often has no alt attribute.

values['alt'] = text
# short description (INPUT)

values['archive~a'] = Sequence(rule=uri_object, regexp=r'\s*,\s*', join_string=',')
# comma-separated archive list (APPLET); deprecated

values['archive'] = Sequence(rule=uri_object, regexp=r'\s+', join_string=' ')
# space-separated list of URIs (OBJECT)

values['axis'] = idrefs_comma
# comma-separated list of related headers (TD, TH)

values['background'] = uri_image
# texture tile for document background (BODY); deprecated

values['bgcolor'] = color
# background color for cells (TABLE); deprecated

values['bgcolor'] = color
# background color for row (TR); deprecated

values['bgcolor'] = color
# cell background color (TD, TH); deprecated

values['bgcolor'] = color
# document background color (BODY); deprecated

values['border'] = pixels
# controls frame width around table (TABLE)

values['border'] = pixels
# link border width (IMG, OBJECT); deprecated

values['cellpadding'] = length
# spacing within cells (TABLE)

values['cellspacing'] = length
# spacing between cells (TABLE)

values['char'] = character
# alignment char, e.g. char=':' (COL, COLGROUP, TBODY, TD, TFOOT, TH, THEAD, TR)

values['charoff'] = length
# offset for alignment char (COL, COLGROUP, TBODY, TD, TFOOT, TH, THEAD, TR)

values['charset'] = charset
# char encoding of linked resource (A, LINK, SCRIPT)

values['checked'] = RegExp(regexp=r'(checked)$')
# for radio buttons and check boxes (INPUT)

values['cite'] = uri
# URI for source document or msg (BLOCKQUOTE, Q)

values['cite'] = uri
# info on reason for change (DEL, INS)

values['class'] = idrefs
# space-separated list of classes (All elements but BASE, BASEFONT, HEAD, HTML, META, PARAM, SCRIPT, STYLE, TITLE)

values['classid'] = uri_object
# identifies an implementation (OBJECT)

values['clear'] = RegExp(regexp=r'(left|all|right|none)$')
# control of text flow (BR); deprecated

values['code'] = text
# applet class file (APPLET); deprecated

values['codebase'] = uri_object
# base URI for classid, data, archive (OBJECT)

values['codebase'] = uri_object
# optional base URI for applet (APPLET); deprecated - for security reasons

values['codetype'] = content_type
# content type for code (OBJECT)

values['color'] = color
# text color (BASEFONT, FONT); deprecated

values['cols'] = multi_lengths
# list of lengths, default: 100% = 1 col (FRAMESET)

values['cols'] = number_required
#  (TEXTAREA)

values['colspan'] = number
# number of cols spanned by cell (TD, TH)

values['compact'] = RegExp(regexp=r'(compact)$')
# reduced interitem spacing (DIR, DL, MENU, OL, UL); deprecated

values['content'] = text_required
# associated information (META)

values['coords'] = coords # Fix: The number and order of values depends on the shape being defined.
# comma-separated list of lengths (AREA)

values['coords'] = coords
# for use with client-side image maps (A)

values['data'] = uri_object
# reference to object's data (OBJECT)

values['datetime'] = datetime
# date and time of change (DEL, INS)

values['declare'] = RegExp(regexp=r'(declare)$')
# declare but don't instantiate flag (OBJECT)

values['defer'] = RegExp(regexp=r'(defer)$')
# UA may defer execution of script (SCRIPT)

values['dir'] = RegExp(regexp=r'(ltr|rtl)$')
# direction for weak/neutral text (All elements but APPLET, BASE, BASEFONT, BDO, BR, FRAME, FRAMESET, IFRAME, PARAM, SCRIPT)

values['dir~r'] = RegExp(regexp=r'(ltr|rtl)$', element_exception=True)
# directionality (BDO)

values['disabled'] = RegExp(regexp=r'(disabled)$')
# unavailable in this context (BUTTON, INPUT, OPTGROUP, OPTION, SELECT, TEXTAREA)

values['enctype'] = content_type
#  (FORM)

values['face'] = idrefs_comma
# comma-separated list of font names (BASEFONT, FONT); deprecated

values['for'] = name
# matches field ID value (LABEL)

values['frame'] = RegExp(regexp=r'(void|above|below|hsides|lhs|rhs|vsides|box|border)$')
# which parts of frame to render (TABLE)

values['frameborder'] = RegExp(regexp=r'(1|0)$')
# request frame borders? (FRAME, IFRAME)

values['headers'] = idrefs
# list of id's for header cells (TD, TH)

values['height'] = length
# frame height (IFRAME)

values['height'] = length
# height for cell (TD, TH); deprecated

values['height'] = length
# override height (IMG, OBJECT)

values['height~r'] = length_required
# initial height (APPLET); deprecated

values['href'] = uri
# URI for linked resource (A, AREA, LINK)

values['href~r'] = uri_required
# Used by href version of tag A

values['href'] = uri
# URI that acts as base URI (BASE)

values['hreflang'] = language_code # Fix: may only be used when href is specified.
# language code (A, LINK)

values['hspace'] = pixels
# horizontal gutter (APPLET, IMG, OBJECT); deprecated

values['http-equiv'] = name
# HTTP response header name (META)

values['id'] = name
# document-wide unique id (All elements but BASE, HEAD, HTML, META, SCRIPT, STYLE, TITLE)

values['ismap'] = RegExp(regexp=r'(ismap)$') # Fix: In the case of IMG, the IMG must be inside an A element and the boolean attribute ismap ([CI]) must be set.
# use server-side image map (IMG, INPUT)

values['label'] = text
# for use in hierarchical menus (OPTION)

values['label~r'] = text_required
# for use in hierarchical menus (OPTGROUP)

values['lang'] = language_code
# language code (All elements but APPLET, BASE, BASEFONT, BR, FRAME, FRAMESET, IFRAME, PARAM, SCRIPT)

values['language'] = text
# predefined script language name (SCRIPT); deprecated

values['link'] = color
# color of links (BODY); deprecated

values['longdesc'] = uri
# link to long description, complements alt (IMG)

values['longdesc'] = uri
# link to long description, complements title (FRAME, IFRAME)

values['marginheight'] = pixels
# margin height in pixels (FRAME, IFRAME)

values['marginwidth'] = pixels
# margin widths in pixels (FRAME, IFRAME)

values['maxlength'] = number
# max chars for text fields (INPUT)

values['media'] = media_descs
# designed for use with these media (STYLE)

values['media'] = media_descs
# for rendering on these media (LINK)

values['method'] = RegExp(regexp=r'(GET|POST)$')
# HTTP method used to submit the form (FORM)

values['multiple'] = RegExp(regexp=r'(multiple)$')
# default is single selection (SELECT)

values['name'] = name
#  (BUTTON, TEXTAREA)

values['name'] = name
# allows applets to find each other (APPLET); deprecated

values['name'] = name
# field name (SELECT)

values['name'] = name
# name of form for scripting (FORM)

values['name'] = name
# name of frame for targetting (FRAME, IFRAME)

values['name'] = name
# name of image for scripting (IMG)

values['name'] = name
# named link end (A)

values['name~r'] = name_required
# Used by anchor version of tag A

values['name'] = name
# submit as part of form (INPUT, OBJECT)

values['name~r'] = name_required
# for reference by usemap (MAP)

values['name~r'] = name_required
# property name (PARAM)

values['name'] = name
# metainformation name (META)

values['nohref'] = RegExp(regexp=r'(nohref)$')
# this region has no action (AREA)

values['noresize'] = RegExp(regexp=r'(noresize)$')
# allow users to resize frames? (FRAME)

values['noshade'] = RegExp(regexp=r'(noshade)$')
#  (HR); deprecated

values['nowrap'] = RegExp(regexp=r'(nowrap)$')
# suppress word wrap (TD, TH); deprecated

values['object'] = name
# serialized applet file (APPLET); deprecated

values['onblur'] = script
# the element lost the focus (A, AREA, BUTTON, INPUT, LABEL, SELECT, TEXTAREA)

values['onchange'] = script
# the element value was changed (INPUT, SELECT, TEXTAREA)

values['onclick'] = script
# a pointer button was clicked (All elements but APPLET, BASE, BASEFONT, BDO, BR, FONT, FRAME, FRAMESET, HEAD, HTML, IFRAME, ISINDEX, META, PARAM, SCRIPT, STYLE, TITLE)

values['ondblclick'] = script
# a pointer button was double clicked (All elements but APPLET, BASE, BASEFONT, BDO, BR, FONT, FRAME, FRAMESET, HEAD, HTML, IFRAME, ISINDEX, META, PARAM, SCRIPT, STYLE, TITLE)

values['onfocus'] = script
# the element got the focus (A, AREA, BUTTON, INPUT, LABEL, SELECT, TEXTAREA)

values['onkeydown'] = script
# a key was pressed down (All elements but APPLET, BASE, BASEFONT, BDO, BR, FONT, FRAME, FRAMESET, HEAD, HTML, IFRAME, ISINDEX, META, PARAM, SCRIPT, STYLE, TITLE)

values['onkeypress'] = script
# a key was pressed and released (All elements but APPLET, BASE, BASEFONT, BDO, BR, FONT, FRAME, FRAMESET, HEAD, HTML, IFRAME, ISINDEX, META, PARAM, SCRIPT, STYLE, TITLE)

values['onkeyup'] = script
# a key was released (All elements but APPLET, BASE, BASEFONT, BDO, BR, FONT, FRAME, FRAMESET, HEAD, HTML, IFRAME, ISINDEX, META, PARAM, SCRIPT, STYLE, TITLE)

values['onload'] = script
# all the frames have been loaded (FRAMESET)

values['onload'] = script
# the document has been loaded (BODY)

values['onmousedown'] = script
# a pointer button was pressed down (All elements but APPLET, BASE, BASEFONT, BDO, BR, FONT, FRAME, FRAMESET, HEAD, HTML, IFRAME, ISINDEX, META, PARAM, SCRIPT, STYLE, TITLE)

values['onmousemove'] = script
# a pointer was moved within (All elements but APPLET, BASE, BASEFONT, BDO, BR, FONT, FRAME, FRAMESET, HEAD, HTML, IFRAME, ISINDEX, META, PARAM, SCRIPT, STYLE, TITLE)

values['onmouseout'] = script
# a pointer was moved away (All elements but APPLET, BASE, BASEFONT, BDO, BR, FONT, FRAME, FRAMESET, HEAD, HTML, IFRAME, ISINDEX, META, PARAM, SCRIPT, STYLE, TITLE)

values['onmouseover'] = script
# a pointer was moved onto (All elements but APPLET, BASE, BASEFONT, BDO, BR, FONT, FRAME, FRAMESET, HEAD, HTML, IFRAME, ISINDEX, META, PARAM, SCRIPT, STYLE, TITLE)

values['onmouseup'] = script
# a pointer button was released (All elements but APPLET, BASE, BASEFONT, BDO, BR, FONT, FRAME, FRAMESET, HEAD, HTML, IFRAME, ISINDEX, META, PARAM, SCRIPT, STYLE, TITLE)

values['onreset'] = script
# the form was reset (FORM)

values['onselect'] = script
# some text was selected (INPUT, TEXTAREA)

values['onsubmit'] = script
# the form was submitted (FORM)

values['onunload'] = script
# all the frames have been removed (FRAMESET)

values['onunload'] = script
# the document has been removed (BODY)

values['profile'] = uris
# named dictionary of meta info (HEAD)

values['prompt'] = text
# prompt message (ISINDEX); deprecated

values['readonly'] = RegExp(regexp=r'(readonly)$')
#  (TEXTAREA)

values['readonly'] = RegExp(regexp=r'(readonly)$')
# for text and passwd (INPUT)

values['rel'] = link_types
# forward link types (A, LINK)

values['rev'] = link_types
# reverse link types (A, LINK)

values['rows'] = multi_lengths
# list of lengths, default: 100% = 1 row (FRAMESET)

values['rows'] = number_required
#  (TEXTAREA)

values['rowspan'] = number
# number of rows spanned by cell (TD, TH)

values['rules'] = RegExp(regexp=r'(none|groups|rows|cols|all)$')
# rulings between rows and cols (TABLE)

values['scheme'] = text
# select form of content (META)

values['scope'] = RegExp(regexp=r'(row|col|rowgroup|colgroup)$')
# scope covered by header cells (TD, TH)

values['scrolling'] = RegExp(regexp=r'(yes|no|auto)$')
# scrollbar or none (FRAME, IFRAME)

values['selected'] = RegExp(regexp=r'(selected)$')
#  (OPTION)

values['shape'] = RegExp(regexp=r'(default|rect|circle|poly)$')
# controls interpretation of coords (AREA)

values['shape'] = RegExp(regexp=r'(default|rect|circle|poly)$')
# for use with client-side image maps (A)

values['size~h'] = pixels
#  (HR); deprecated

values['size~f'] = RegExp(regexp=r'([-+]?[1-7])$')
# [+|-]nn e.g. size=+1, size=4 (FONT); deprecated

values['size'] = number
# specific to each type of field (INPUT)

values['size~b'] = RegExp(regexp=r'([-+]?[1-7])$', element_exception=True)
# base font size for FONT elements (BASEFONT); deprecated

values['size'] = number
# rows visible (SELECT)

values['span'] = positive_number
# COL attributes affect N columns (COL)

values['span'] = positive_number
# default number of columns in group (COLGROUP)

values['src'] = uri
# URI for an external script (SCRIPT)

values['src~i'] = uri_image
# for fields with images (INPUT)

values['src~f'] = uri_object
# source of frame content (FRAME, IFRAME)

values['src~r'] = uri_image_required
# URI of image to embed (IMG)

values['standby'] = text
# message to show while loading (OBJECT)

values['start'] = number
# starting sequence number (OL); deprecated

values['style'] = style_sheet
# associated style info (All elements but BASE, BASEFONT, HEAD, HTML, META, PARAM, SCRIPT, STYLE, TITLE)

values['summary'] = text
# purpose/structure for speech output (TABLE)

values['tabindex'] = number
# position in tabbing order (A, AREA, BUTTON, INPUT, OBJECT, SELECT, TEXTAREA)

values['target'] = frame_target
# render in this frame (A, AREA, BASE, FORM, LINK)

values['text'] = color
# document text color (BODY); deprecated

values['title'] = text
# advisory title (All elements but BASE, BASEFONT, HEAD, HTML, META, PARAM, SCRIPT, TITLE)

values['type'] = content_type
# advisory content type (A, LINK)

values['type'] = content_type
# content type for data (OBJECT)

values['type'] = content_type # Fix: only in the case where valuetype is set to "ref".
# content type for value when valuetype=ref (PARAM)

values['type~r'] = content_type_required
# content type of script language (SCRIPT)

values['type~r'] = content_type_required
# content type of style language (STYLE)

values['type~i'] = RegExp(regexp=r'(text|password|checkbox|radio|submit|reset|file|hidden|image|button)$')
# what kind of widget is needed (INPUT)

values['type~l'] = RegExp(regexp=r'(1|a|A|i|I|disc|square|circle)$')
# list item style (LI); deprecated

values['type~o'] = RegExp(regexp=r'(1|a|A|i|I)$')
# numbering style (OL); deprecated

values['type~u'] = RegExp(regexp=r'(disc|square|circle)$')
# bullet style (UL); deprecated

values['type~b'] = RegExp(regexp=r'(button|submit|reset)$')
# for use as form button (BUTTON)

values['usemap'] = uri
# use client-side image map (IMG, INPUT, OBJECT)

values['valign'] = RegExp(regexp=r'(top|middle|bottom|baseline)$')
# vertical alignment in cells (COL, COLGROUP, TBODY, TD, TFOOT, TH, THEAD, TR)

values['value'] = text # Fix: It is optional except when the type attribute has the value "radio" or "checkbox".
# Specify for radio buttons and checkboxes (INPUT)

values['value'] = text
# defaults to element content (OPTION)

values['value'] = text
# property value (PARAM)

values['value'] = text
# sent to server when submitted (BUTTON)

values['value~l'] = number
# reset sequence number (LI); deprecated

values['valuetype'] = RegExp(regexp=r'(data|ref|object)$')
# How to interpret value (PARAM)

values['version'] = uri
# Constant (HTML); deprecated

values['vlink'] = color
# color of visited links (BODY); deprecated

values['vspace'] = pixels
# vertical gutter (APPLET, IMG, OBJECT); deprecated

values['width'] = length
#  (HR); deprecated

values['width'] = length
# frame width (IFRAME)

values['width'] = length
# override width (IMG, OBJECT)

values['width'] = length
# table width (TABLE)

values['width'] = length
# width for cell (TD, TH); deprecated

values['width~r'] = length_required
# initial width (APPLET); deprecated

values['width~c'] = multi_length
# column width specification (COL)

values['width~c'] = multi_length
# default width for enclosed COLs (COLGROUP)

values['width~p'] = number
#  (PRE); deprecated
