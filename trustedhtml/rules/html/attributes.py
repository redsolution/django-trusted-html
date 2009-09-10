"""
Index of Attributes
http://www.w3.org/TR/REC-html40/index/attributes.html

Attributes for different elements can have different validation mechanism.
In such case we will use different names:
name of attribute followed immediately by an ':' character followed immediately
by [a-z] character.

Attributes for different elements can have same validation mechanism,
but separated in specification because of meaning.
In such case we will assign same values to the same attributes.
We do it to parse descriptions and generate ``map.py``.
"""

attributes = {}

attributes['abbr'] = text
# abbreviation for header cell (TD, TH) 

attributes['accept-charset'] = charsets
# list of supported charsets (FORM) 

attributes['accept'] = content_types
# list of MIME types for file upload (FORM, INPUT) 

attributes['accesskey'] = character
# accessibility key character (A, AREA, BUTTON, INPUT, LABEL, LEGEND, TEXTAREA) 

attributes['action'] = uri_required
# server-side form handler (FORM) 

attributes['align:c'] = RegExp(regexp=r'(top|bottom|left|right)$')
# relative to table (CAPTION) ; deprecated

attributes['align:i'] = RegExp(regexp=r'(top|middle|bottom|left|right)$')
# vertical or horizontal alignment (APPLET, IFRAME, IMG, INPUT, OBJECT) ; deprecated

attributes['align:l'] = RegExp(regexp=r'(top|bottom|left|right)$')
# relative to fieldset (LEGEND) ; deprecated

attributes['align:t'] = RegExp(regexp=r'(left|center|right)$')
# table position relative to window (TABLE) ; deprecated

attributes['align:h'] = RegExp(regexp=r'(left|center|right)$')
#  (HR) ; deprecated

attributes['align:d'] = RegExp(regexp=r'(left|center|right|justify)$')
# align, text alignment (DIV, H1, H2, H3, H4, H5, H6, P) ; deprecated

attributes['align'] = RegExp(regexp=r'(left|center|right|justify|char)$')
#  (COL, COLGROUP, TBODY, TD, TFOOT, TH, THEAD, TR) 

attributes['alink'] = color
# color of selected links (BODY) ; deprecated

attributes['alt'] = text
# short description (APPLET) ; deprecated

attributes['alt:r'] = text_required
# short description (AREA, IMG) 

attributes['alt'] = text
# short description (INPUT) 

attributes['archive:a'] = Sequence(rule=uri, regexp=r'\s*,\s*', join_string=',')
# comma-separated archive list (APPLET) ; deprecated

attributes['archive'] = Sequence(rule=uri, regexp=r'\s+', join_string=' ')
# space-separated list of URIs (OBJECT) 

attributes['axis'] = idrefs_comma
# comma-separated list of related headers (TD, TH) 

attributes['background'] = uri_image
# texture tile for document background (BODY) ; deprecated

attributes['bgcolor'] = color
# background color for cells (TABLE) ; deprecated

attributes['bgcolor'] = color
# background color for row (TR) ; deprecated

attributes['bgcolor'] = color
# cell background color (TD, TH) ; deprecated

attributes['bgcolor'] = color
# document background color (BODY) ; deprecated

attributes['border'] = pixels
# controls frame width around table (TABLE) 

attributes['border'] = pixels
# link border width (IMG, OBJECT) ; deprecated

attributes['cellpadding'] = length
# spacing within cells (TABLE) 

attributes['cellspacing'] = length
# spacing between cells (TABLE) 

attributes['char'] = character
# alignment char, e.g. char=':' (COL, COLGROUP, TBODY, TD, TFOOT, TH, THEAD, TR) 

attributes['charoff'] = length
# offset for alignment char (COL, COLGROUP, TBODY, TD, TFOOT, TH, THEAD, TR) 

attributes['charset'] = charset
# char encoding of linked resource (A, LINK, SCRIPT) 

attributes['checked'] = RegExp(regexp=r'(checked)$')
# for radio buttons and check boxes (INPUT) 

attributes['cite'] = uri
# URI for source document or msg (BLOCKQUOTE, Q) 

attributes['cite'] = uri
# info on reason for change (DEL, INS) 

attributes['class'] = idrefs
# space-separated list of classes (All elements but BASE, BASEFONT, HEAD, HTML, META, PARAM, SCRIPT, STYLE, TITLE) 

attributes['classid'] = uri
# identifies an implementation (OBJECT) 

attributes['clear'] = RegExp(regexp=r'(left|all|right|none)$')
# control of text flow (BR) ; deprecated

attributes['code'] = text
# applet class file (APPLET) ; deprecated

attributes['codebase'] = uri
# base URI for classid, data, archive (OBJECT) 

attributes['codebase'] = uri
# optional base URI for applet (APPLET) ; deprecated

attributes['codetype'] = content_type
# content type for code (OBJECT) 

attributes['color'] = color
# text color (BASEFONT, FONT) ; deprecated

attributes['cols'] = multi_lengths
# list of lengths, default: 100% (1 col) (FRAMESET) 

attributes['cols'] = number_required
#  (TEXTAREA) 

attributes['colspan'] = number
# number of cols spanned by cell (TD, TH) 

attributes['compact'] = RegExp(regexp=r'(compact)$')
# reduced interitem spacing (DIR, DL, MENU, OL, UL) ; deprecated

attributes['content'] = text_required
# associated information (META) 

attributes['coords'] = coords # Fix: The number and order of values depends on the shape being defined.
# comma-separated list of lengths (AREA) 

attributes['coords'] = coords
# for use with client-side image maps (A) 

attributes['data'] = uri
# reference to object's data (OBJECT) 

attributes['datetime'] = datetime
# date and time of change (DEL, INS) 

attributes['declare'] = RegExp(regexp=r'(declare)$')
# declare but don't instantiate flag (OBJECT) 

attributes['defer'] = RegExp(regexp=r'(defer)$')
# UA may defer execution of script (SCRIPT) 

attributes['dir'] = RegExp(regexp=r'(ltr|rtl)$')
# direction for weak/neutral text (All elements but APPLET, BASE, BASEFONT, BDO, BR, FRAME, FRAMESET, IFRAME, PARAM, SCRIPT) 

attributes['dir:r'] = RegExp(regexp=r'(ltr|rtl)$', required=True)
# directionality (BDO) 

attributes['disabled'] = RegExp(regexp=r'(disabled)$')
# unavailable in this context (BUTTON, INPUT, OPTGROUP, OPTION, SELECT, TEXTAREA) 

attributes['enctype'] = content_type
#  (FORM) 

attributes['face'] = idrefs_comma
# comma-separated list of font names (BASEFONT, FONT) ; deprecated

attributes['for'] = idref
# matches field ID value (LABEL) 

attributes['frame'] = RegExp(regexp=r'(void|above|below|hsides|lhs|rhs|vsides|box|border)$')
# which parts of frame to render (TABLE) 

attributes['frameborder'] = RegExp(regexp=r'(1|0)$')
# request frame borders? (FRAME, IFRAME) 

attributes['headers'] = idrefs
# list of id's for header cells (TD, TH) 

attributes['height'] = length
# frame height (IFRAME) 

attributes['height'] = length
# height for cell (TD, TH) ; deprecated

attributes['height'] = length
# override height (IMG, OBJECT) 

attributes['height:r'] = length_required
# initial height (APPLET) ; deprecated

attributes['href'] = uri
# URI for linked resource (A, AREA, LINK) 

attributes['href'] = uri
# URI that acts as base URI (BASE) 

attributes['hreflang'] = language_code # Fix: may only be used when href is specified.
# language code (A, LINK) 

attributes['hspace'] = pixels
# horizontal gutter (APPLET, IMG, OBJECT) ; deprecated

attributes['http-equiv'] = name
# HTTP response header name (META) 

attributes['id'] = name
# document-wide unique id (All elements but BASE, HEAD, HTML, META, SCRIPT, STYLE, TITLE) 

attributes['ismap'] = RegExp(regexp=r'(ismap)$') # Fix: In the case of IMG, the IMG must be inside an A element and the boolean attribute ismap ([CI]) must be set. 
# use server-side image map (IMG, INPUT) 

attributes['label'] = text
# for use in hierarchical menus (OPTION) 

attributes['label:r'] = text_required
# for use in hierarchical menus (OPTGROUP) 

attributes['lang'] = language_code
# language code (All elements but APPLET, BASE, BASEFONT, BR, FRAME, FRAMESET, IFRAME, PARAM, SCRIPT) 

attributes['language'] = text
# predefined script language name (SCRIPT) ; deprecated

attributes['link'] = color
# color of links (BODY) ; deprecated

attributes['longdesc'] = uri
# link to long description (complements alt) (IMG) 

attributes['longdesc'] = uri
# link to long description (complements title) (FRAME, IFRAME) 

attributes['marginheight'] = pixels
# margin height in pixels (FRAME, IFRAME) 

attributes['marginwidth'] = pixels
# margin widths in pixels (FRAME, IFRAME) 

attributes['maxlength'] = number
# max chars for text fields (INPUT) 

attributes['media'] = media_descs
# designed for use with these media (STYLE) 

attributes['media'] = media_descs
# for rendering on these media (LINK) 

attributes['method'] = RegExp(regexp=r'(GET|POST)$')
# HTTP method used to submit the form (FORM) 

attributes['multiple'] = RegExp(regexp=r'(multiple)$')
# default is single selection (SELECT) 

attributes['name'] = name
#  (BUTTON, TEXTAREA) 

attributes['name'] = name
# allows applets to find each other (APPLET) ; deprecated

attributes['name'] = name
# field name (SELECT) 

attributes['name'] = name
# name of form for scripting (FORM) 

attributes['name'] = name
# name of frame for targetting (FRAME, IFRAME) 

attributes['name'] = name
# name of image for scripting (IMG) 

attributes['name'] = name
# named link end (A) 

attributes['name'] = name
# submit as part of form (INPUT, OBJECT) 

attributes['name:r'] = name_required
# for reference by usemap (MAP) 

attributes['name:r'] = name_required
# property name (PARAM) 

attributes['name'] = name
# metainformation name (META) 

attributes['nohref'] = RegExp(regexp=r'(nohref)$')
# this region has no action (AREA) 

attributes['noresize'] = RegExp(regexp=r'(noresize)$')
# allow users to resize frames? (FRAME) 

attributes['noshade'] = RegExp(regexp=r'(noshade)$')
#  (HR) ; deprecated

attributes['nowrap'] = RegExp(regexp=r'(nowrap)$')
# suppress word wrap (TD, TH) ; deprecated

attributes['object'] = name
# serialized applet file (APPLET) ; deprecated

attributes['onblur'] = script
# the element lost the focus (A, AREA, BUTTON, INPUT, LABEL, SELECT, TEXTAREA) 

attributes['onchange'] = script
# the element value was changed (INPUT, SELECT, TEXTAREA) 

attributes['onclick'] = script
# a pointer button was clicked (All elements but APPLET, BASE, BASEFONT, BDO, BR, FONT, FRAME, FRAMESET, HEAD, HTML, IFRAME, ISINDEX, META, PARAM, SCRIPT, STYLE, TITLE) 

attributes['ondblclick'] = script
# a pointer button was double clicked (All elements but APPLET, BASE, BASEFONT, BDO, BR, FONT, FRAME, FRAMESET, HEAD, HTML, IFRAME, ISINDEX, META, PARAM, SCRIPT, STYLE, TITLE) 

attributes['onfocus'] = script
# the element got the focus (A, AREA, BUTTON, INPUT, LABEL, SELECT, TEXTAREA) 

attributes['onkeydown'] = script
# a key was pressed down (All elements but APPLET, BASE, BASEFONT, BDO, BR, FONT, FRAME, FRAMESET, HEAD, HTML, IFRAME, ISINDEX, META, PARAM, SCRIPT, STYLE, TITLE) 

attributes['onkeypress'] = script
# a key was pressed and released (All elements but APPLET, BASE, BASEFONT, BDO, BR, FONT, FRAME, FRAMESET, HEAD, HTML, IFRAME, ISINDEX, META, PARAM, SCRIPT, STYLE, TITLE) 

attributes['onkeyup'] = script
# a key was released (All elements but APPLET, BASE, BASEFONT, BDO, BR, FONT, FRAME, FRAMESET, HEAD, HTML, IFRAME, ISINDEX, META, PARAM, SCRIPT, STYLE, TITLE) 

attributes['onload'] = script
# all the frames have been loaded (FRAMESET) 

attributes['onload'] = script
# the document has been loaded (BODY) 

attributes['onmousedown'] = script
# a pointer button was pressed down (All elements but APPLET, BASE, BASEFONT, BDO, BR, FONT, FRAME, FRAMESET, HEAD, HTML, IFRAME, ISINDEX, META, PARAM, SCRIPT, STYLE, TITLE) 

attributes['onmousemove'] = script
# a pointer was moved within (All elements but APPLET, BASE, BASEFONT, BDO, BR, FONT, FRAME, FRAMESET, HEAD, HTML, IFRAME, ISINDEX, META, PARAM, SCRIPT, STYLE, TITLE) 

attributes['onmouseout'] = script
# a pointer was moved away (All elements but APPLET, BASE, BASEFONT, BDO, BR, FONT, FRAME, FRAMESET, HEAD, HTML, IFRAME, ISINDEX, META, PARAM, SCRIPT, STYLE, TITLE) 

attributes['onmouseover'] = script
# a pointer was moved onto (All elements but APPLET, BASE, BASEFONT, BDO, BR, FONT, FRAME, FRAMESET, HEAD, HTML, IFRAME, ISINDEX, META, PARAM, SCRIPT, STYLE, TITLE) 

attributes['onmouseup'] = script
# a pointer button was released (All elements but APPLET, BASE, BASEFONT, BDO, BR, FONT, FRAME, FRAMESET, HEAD, HTML, IFRAME, ISINDEX, META, PARAM, SCRIPT, STYLE, TITLE) 

attributes['onreset'] = script
# the form was reset (FORM) 

attributes['onselect'] = script
# some text was selected (INPUT, TEXTAREA) 

attributes['onsubmit'] = script
# the form was submitted (FORM) 

attributes['onunload'] = script
# all the frames have been removed (FRAMESET) 

attributes['onunload'] = script
# the document has been removed (BODY) 

attributes['profile'] = uris
# named dictionary of meta info (HEAD) 

attributes['prompt'] = text
# prompt message (ISINDEX) ; deprecated

attributes['readonly'] = RegExp(regexp=r'(readonly)$')
#  (TEXTAREA) 

attributes['readonly'] = RegExp(regexp=r'(readonly)$')
# for text and passwd (INPUT) 

attributes['rel'] = link_types
# forward link types (A, LINK) 

attributes['rev'] = link_types
# reverse link types (A, LINK) 

attributes['rows'] = multi_lengths
# list of lengths, default: 100% (1 row) (FRAMESET) 

attributes['rows'] = number_required
#  (TEXTAREA) 

attributes['rowspan'] = number
# number of rows spanned by cell (TD, TH) 

attributes['rules'] = RegExp(regexp=r'(none|groups|rows|cols|all)$')
# rulings between rows and cols (TABLE) 

attributes['scheme'] = name
# select form of content (META) 

attributes['scope'] = RegExp(regexp=r'(row|col|rowgroup|colgroup)$')
# scope covered by header cells (TD, TH) 

attributes['scrolling'] = RegExp(regexp=r'(yes|no|auto)$')
# scrollbar or none (FRAME, IFRAME) 

attributes['selected'] = RegExp(regexp=r'(selected)$')
#  (OPTION) 

attributes['shape'] = RegExp(regexp=r'(default|rect|circle|poly)$')
# controls interpretation of coords (AREA) 

attributes['shape'] = RegExp(regexp=r'(default|rect|circle|poly)$')
# for use with client-side image maps (A) 

attributes['size:h'] = pixels
#  (HR) ; deprecated

attributes['size:f'] = RegExp(regexp=r'([-+]?[1-7])$')
# [+|-]nn e.g. size=+1, size=4 (FONT) ; deprecated

attributes['size'] = number
# specific to each type of field (INPUT) 

attributes['size:b'] = RegExp(regexp=r'([-+]?[1-7])$', required=True)
# base font size for FONT elements (BASEFONT) ; deprecated

attributes['size'] = number
# rows visible (SELECT) 

attributes['span'] = positive_int
# COL attributes affect N columns (COL) 

attributes['span'] = positive_int
# default number of columns in group (COLGROUP) 

attributes['src'] = uri
# URI for an external script (SCRIPT) 

attributes['src:i'] = uri_image
# for fields with images (INPUT) 

attributes['src'] = uri
# source of frame content (FRAME, IFRAME) 

attributes['src:r'] = uri_image_required
# URI of image to embed (IMG) 

attributes['standby'] = text
# message to show while loading (OBJECT) 

attributes['start'] = number
# starting sequence number (OL) ; deprecated

attributes['style'] = style_sheet
# associated style info (All elements but BASE, BASEFONT, HEAD, HTML, META, PARAM, SCRIPT, STYLE, TITLE) 

attributes['summary'] = text
# purpose/structure for speech output (TABLE) 

attributes['tabindex'] = number
# position in tabbing order (A, AREA, BUTTON, INPUT, OBJECT, SELECT, TEXTAREA) 

attributes['target'] = frame_target
# render in this frame (A, AREA, BASE, FORM, LINK) 

attributes['text'] = color
# document text color (BODY) ; deprecated

attributes['title'] = text
# advisory title (All elements but BASE, BASEFONT, HEAD, HTML, META, PARAM, SCRIPT, TITLE) 

attributes['type'] = content_type
# advisory content type (A, LINK) 

attributes['type'] = content_type
# content type for data (OBJECT) 

attributes['type'] = content_type # Fix: only in the case where valuetype is set to "ref".
# content type for value when valuetype=ref (PARAM) 

attributes['type:r'] = content_type_required
# content type of script language (SCRIPT) 

attributes['type:r'] = content_type_required
# content type of style language (STYLE) 

attributes['type:i'] = RegExp(regexp=r'(text|password|checkbox|radio|submit|reset|file|hidden|image|button)$')
# what kind of widget is needed (INPUT) 

attributes['type:l'] = RegExp(regexp=r'(1|a|A|i|I|disc|square|circle)$')
# list item style (LI) ; deprecated

attributes['type:o'] = RegExp(regexp=r'(1|a|A|i|I)$')
# numbering style (OL) ; deprecated

attributes['type:u'] = RegExp(regexp=r'(disc|square|circle)$')
# bullet style (UL) ; deprecated

attributes['type'] = RegExp(regexp=r'(button|submit|reset)$')
# for use as form button (BUTTON) 

attributes['usemap'] = uri
# use client-side image map (IMG, INPUT, OBJECT) 

attributes['valign'] = RegExp(regexp=r'(top|middle|bottom|baseline)$')
# vertical alignment in cells (COL, COLGROUP, TBODY, TD, TFOOT, TH, THEAD, TR) 

attributes['value'] = text # Fix: It is optional except when the type attribute has the value "radio" or "checkbox".
# Specify for radio buttons and checkboxes (INPUT) 

attributes['value'] = text
# defaults to element content (OPTION) 

attributes['value'] = text
# property value (PARAM) 

attributes['value'] = text
# sent to server when submitted (BUTTON) 

attributes['value:l'] = number
# reset sequence number (LI) ; deprecated

attributes['valuetype'] = RegExp(regexp=r'(data|ref|object)$')
# How to interpret value (PARAM) 

attributes['version'] = uri
# Constant (HTML) ; deprecated

attributes['vlink'] = color
# color of visited links (BODY) ; deprecated

attributes['vspace'] = pixels
# vertical gutter (APPLET, IMG, OBJECT) ; deprecated

attributes['width'] = length
#  (HR) ; deprecated

attributes['width'] = length
# frame width (IFRAME) 

attributes['width'] = length
# override width (IMG, OBJECT) 

attributes['width'] = length
# table width (TABLE) 

attributes['width'] = length
# width for cell (TD, TH) ; deprecated

attributes['width:r'] = length_required
# initial width (APPLET) ; deprecated

attributes['width:c'] = multi_length
# column width specification (COL) 

attributes['width:c'] = multi_length
# default width for enclosed COLs (COLGROUP) 

attributes['width:p'] = number
#  (PRE) ; deprecated
