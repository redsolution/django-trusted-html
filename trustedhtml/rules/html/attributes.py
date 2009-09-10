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

attributes['abbr'] = %Text;
# abbreviation for header cell (TD, TH) 

attributes['accept-charset'] = %Charsets;
# list of supported charsets (FORM) 

attributes['accept'] = %ContentTypes;
# list of MIME types for file upload (FORM, INPUT) 

attributes['accesskey'] = %Character;
# accessibility key character (A, AREA, BUTTON, INPUT, LABEL, LEGEND, TEXTAREA) 

attributes['action'] = %URI;#REQUIRED
# server-side form handler (FORM) 

attributes['align'] = %CAlign;
# relative to table (CAPTION) ; deprecated

attributes['align'] = %IAlign;
# vertical or horizontal alignment (APPLET, IFRAME, IMG, INPUT, OBJECT) ; deprecated

attributes['align'] = %LAlign;
# relative to fieldset (LEGEND) ; deprecated

attributes['align'] = %TAlign;
# table position relative to window (TABLE) ; deprecated

attributes['align'] = RegExp(regexp=r'(left | center | right)')
#  (HR) ; deprecated

attributes['align'] = RegExp(regexp=r'(left | center | right | justify)')
# align, text alignment (DIV, H1, H2, H3, H4, H5, H6, P) ; deprecated

attributes['align'] = RegExp(regexp=r'(left | center | right | justify | char)')
#  (COL, COLGROUP, TBODY, TD, TFOOT, TH, THEAD, TR) 

attributes['alink'] = %Color;
# color of selected links (BODY) ; deprecated

attributes['alt'] = %Text;
# short description (APPLET) ; deprecated

attributes['alt'] = %Text;#REQUIRED
# short description (AREA, IMG) 

attributes['alt'] = CDATA
# short description (INPUT) 

attributes['archive'] = CDATA
# comma-separated archive list (APPLET) ; deprecated

attributes['archive'] = CDATA
# space-separated list of URIs (OBJECT) 

attributes['axis'] = CDATA
# comma-separated list of related headers (TD, TH) 

attributes['background'] = %URI;
# texture tile for document background (BODY) ; deprecated

attributes['bgcolor'] = %Color;
# background color for cells (TABLE) ; deprecated

attributes['bgcolor'] = %Color;
# background color for row (TR) ; deprecated

attributes['bgcolor'] = %Color;
# cell background color (TD, TH) ; deprecated

attributes['bgcolor'] = %Color;
# document background color (BODY) ; deprecated

attributes['border'] = %Pixels;
# controls frame width around table (TABLE) 

attributes['border'] = %Pixels;
# link border width (IMG, OBJECT) ; deprecated

attributes['cellpadding'] = %Length;
# spacing within cells (TABLE) 

attributes['cellspacing'] = %Length;
# spacing between cells (TABLE) 

attributes['char'] = %Character;
# alignment char, e.g. char=':' (COL, COLGROUP, TBODY, TD, TFOOT, TH, THEAD, TR) 

attributes['charoff'] = %Length;
# offset for alignment char (COL, COLGROUP, TBODY, TD, TFOOT, TH, THEAD, TR) 

attributes['charset'] = %Charset;
# char encoding of linked resource (A, LINK, SCRIPT) 

attributes['checked'] = RegExp(regexp=r'(checked)')
# for radio buttons and check boxes (INPUT) 

attributes['cite'] = %URI;
# URI for source document or msg (BLOCKQUOTE, Q) 

attributes['cite'] = %URI;
# info on reason for change (DEL, INS) 

attributes['class'] = CDATA
# space-separated list of classes (All elements but BASE, BASEFONT, HEAD, HTML, META, PARAM, SCRIPT, STYLE, TITLE) 

attributes['classid'] = %URI;
# identifies an implementation (OBJECT) 

attributes['clear'] = RegExp(regexp=r'(left | all | right | none)')none
# control of text flow (BR) ; deprecated

attributes['code'] = CDATA
# applet class file (APPLET) ; deprecated

attributes['codebase'] = %URI;
# base URI for classid, data, archive (OBJECT) 

attributes['codebase'] = %URI;
# optional base URI for applet (APPLET) ; deprecated

attributes['codetype'] = %ContentType;
# content type for code (OBJECT) 

attributes['color'] = %Color;
# text color (BASEFONT, FONT) ; deprecated

attributes['cols'] = %MultiLengths;
# list of lengths, default: 100% (1 col) (FRAMESET) 

attributes['cols'] = NUMBER#REQUIRED
#  (TEXTAREA) 

attributes['colspan'] = NUMBER1
# number of cols spanned by cell (TD, TH) 

attributes['compact'] = RegExp(regexp=r'(compact)')
# reduced interitem spacing (DIR, DL, MENU, OL, UL) ; deprecated

attributes['content'] = CDATA#REQUIRED
# associated information (META) 

attributes['coords'] = %Coords;
# comma-separated list of lengths (AREA) 

attributes['coords'] = %Coords;
# for use with client-side image maps (A) 

attributes['data'] = %URI;
# reference to object's data (OBJECT) 

attributes['datetime'] = %Datetime;
# date and time of change (DEL, INS) 

attributes['declare'] = RegExp(regexp=r'(declare)')
# declare but don't instantiate flag (OBJECT) 

attributes['defer'] = RegExp(regexp=r'(defer)')
# UA may defer execution of script (SCRIPT) 

attributes['dir'] = RegExp(regexp=r'(ltr | rtl)')
# direction for weak/neutral text (All elements but APPLET, BASE, BASEFONT, BDO, BR, FRAME, FRAMESET, IFRAME, PARAM, SCRIPT) 

attributes['dir'] = RegExp(regexp=r'(ltr | rtl)')#REQUIRED
# directionality (BDO) 

attributes['disabled'] = RegExp(regexp=r'(disabled)')
# unavailable in this context (BUTTON, INPUT, OPTGROUP, OPTION, SELECT, TEXTAREA) 

attributes['enctype'] = %ContentType;application/x-www- form-urlencoded
#  (FORM) 

attributes['face'] = CDATA
# comma-separated list of font names (BASEFONT, FONT) ; deprecated

attributes['for'] = IDREF
# matches field ID value (LABEL) 

attributes['frame'] = %TFrame;
# which parts of frame to render (TABLE) 

attributes['frameborder'] = RegExp(regexp=r'(1 | 0)')1
# request frame borders? (FRAME, IFRAME) 

attributes['headers'] = IDREFS
# list of id's for header cells (TD, TH) 

attributes['height'] = %Length;
# frame height (IFRAME) 

attributes['height'] = %Length;
# height for cell (TD, TH) ; deprecated

attributes['height'] = %Length;
# override height (IMG, OBJECT) 

attributes['height'] = %Length;#REQUIRED
# initial height (APPLET) ; deprecated

attributes['href'] = %URI;
# URI for linked resource (A, AREA, LINK) 

attributes['href'] = %URI;
# URI that acts as base URI (BASE) 

attributes['hreflang'] = %LanguageCode;
# language code (A, LINK) 

attributes['hspace'] = %Pixels;
# horizontal gutter (APPLET, IMG, OBJECT) ; deprecated

attributes['http-equiv'] = NAME
# HTTP response header name (META) 

attributes['id'] = ID
# document-wide unique id (All elements but BASE, HEAD, HTML, META, SCRIPT, STYLE, TITLE) 

attributes['ismap'] = RegExp(regexp=r'(ismap)')
# use server-side image map (IMG, INPUT) 

attributes['label'] = %Text;
# for use in hierarchical menus (OPTION) 

attributes['label'] = %Text;#REQUIRED
# for use in hierarchical menus (OPTGROUP) 

attributes['lang'] = %LanguageCode;
# language code (All elements but APPLET, BASE, BASEFONT, BR, FRAME, FRAMESET, IFRAME, PARAM, SCRIPT) 

attributes['language'] = CDATA
# predefined script language name (SCRIPT) ; deprecated

attributes['link'] = %Color;
# color of links (BODY) ; deprecated

attributes['longdesc'] = %URI;
# link to long description (complements alt) (IMG) 

attributes['longdesc'] = %URI;
# link to long description (complements title) (FRAME, IFRAME) 

attributes['marginheight'] = %Pixels;
# margin height in pixels (FRAME, IFRAME) 

attributes['marginwidth'] = %Pixels;
# margin widths in pixels (FRAME, IFRAME) 

attributes['maxlength'] = NUMBER
# max chars for text fields (INPUT) 

attributes['media'] = %MediaDesc;
# designed for use with these media (STYLE) 

attributes['media'] = %MediaDesc;
# for rendering on these media (LINK) 

attributes['method'] = RegExp(regexp=r'(GET | POST)')GET
# HTTP method used to submit the form (FORM) 

attributes['multiple'] = RegExp(regexp=r'(multiple)')
# default is single selection (SELECT) 

attributes['name'] = CDATA
#  (BUTTON, TEXTAREA) 

attributes['name'] = CDATA
# allows applets to find each other (APPLET) ; deprecated

attributes['name'] = CDATA
# field name (SELECT) 

attributes['name'] = CDATA
# name of form for scripting (FORM) 

attributes['name'] = CDATA
# name of frame for targetting (FRAME, IFRAME) 

attributes['name'] = CDATA
# name of image for scripting (IMG) 

attributes['name'] = CDATA
# named link end (A) 

attributes['name'] = CDATA
# submit as part of form (INPUT, OBJECT) 

attributes['name'] = CDATA#REQUIRED
# for reference by usemap (MAP) 

attributes['name'] = CDATA#REQUIRED
# property name (PARAM) 

attributes['name'] = NAME
# metainformation name (META) 

attributes['nohref'] = RegExp(regexp=r'(nohref)')
# this region has no action (AREA) 

attributes['noresize'] = RegExp(regexp=r'(noresize)')
# allow users to resize frames? (FRAME) 

attributes['noshade'] = RegExp(regexp=r'(noshade)')
#  (HR) ; deprecated

attributes['nowrap'] = RegExp(regexp=r'(nowrap)')
# suppress word wrap (TD, TH) ; deprecated

attributes['object'] = CDATA
# serialized applet file (APPLET) ; deprecated

attributes['onblur'] = %Script;
# the element lost the focus (A, AREA, BUTTON, INPUT, LABEL, SELECT, TEXTAREA) 

attributes['onchange'] = %Script;
# the element value was changed (INPUT, SELECT, TEXTAREA) 

attributes['onclick'] = %Script;
# a pointer button was clicked (All elements but APPLET, BASE, BASEFONT, BDO, BR, FONT, FRAME, FRAMESET, HEAD, HTML, IFRAME, ISINDEX, META, PARAM, SCRIPT, STYLE, TITLE) 

attributes['ondblclick'] = %Script;
# a pointer button was double clicked (All elements but APPLET, BASE, BASEFONT, BDO, BR, FONT, FRAME, FRAMESET, HEAD, HTML, IFRAME, ISINDEX, META, PARAM, SCRIPT, STYLE, TITLE) 

attributes['onfocus'] = %Script;
# the element got the focus (A, AREA, BUTTON, INPUT, LABEL, SELECT, TEXTAREA) 

attributes['onkeydown'] = %Script;
# a key was pressed down (All elements but APPLET, BASE, BASEFONT, BDO, BR, FONT, FRAME, FRAMESET, HEAD, HTML, IFRAME, ISINDEX, META, PARAM, SCRIPT, STYLE, TITLE) 

attributes['onkeypress'] = %Script;
# a key was pressed and released (All elements but APPLET, BASE, BASEFONT, BDO, BR, FONT, FRAME, FRAMESET, HEAD, HTML, IFRAME, ISINDEX, META, PARAM, SCRIPT, STYLE, TITLE) 

attributes['onkeyup'] = %Script;
# a key was released (All elements but APPLET, BASE, BASEFONT, BDO, BR, FONT, FRAME, FRAMESET, HEAD, HTML, IFRAME, ISINDEX, META, PARAM, SCRIPT, STYLE, TITLE) 

attributes['onload'] = %Script;
# all the frames have been loaded (FRAMESET) 

attributes['onload'] = %Script;
# the document has been loaded (BODY) 

attributes['onmousedown'] = %Script;
# a pointer button was pressed down (All elements but APPLET, BASE, BASEFONT, BDO, BR, FONT, FRAME, FRAMESET, HEAD, HTML, IFRAME, ISINDEX, META, PARAM, SCRIPT, STYLE, TITLE) 

attributes['onmousemove'] = %Script;
# a pointer was moved within (All elements but APPLET, BASE, BASEFONT, BDO, BR, FONT, FRAME, FRAMESET, HEAD, HTML, IFRAME, ISINDEX, META, PARAM, SCRIPT, STYLE, TITLE) 

attributes['onmouseout'] = %Script;
# a pointer was moved away (All elements but APPLET, BASE, BASEFONT, BDO, BR, FONT, FRAME, FRAMESET, HEAD, HTML, IFRAME, ISINDEX, META, PARAM, SCRIPT, STYLE, TITLE) 

attributes['onmouseover'] = %Script;
# a pointer was moved onto (All elements but APPLET, BASE, BASEFONT, BDO, BR, FONT, FRAME, FRAMESET, HEAD, HTML, IFRAME, ISINDEX, META, PARAM, SCRIPT, STYLE, TITLE) 

attributes['onmouseup'] = %Script;
# a pointer button was released (All elements but APPLET, BASE, BASEFONT, BDO, BR, FONT, FRAME, FRAMESET, HEAD, HTML, IFRAME, ISINDEX, META, PARAM, SCRIPT, STYLE, TITLE) 

attributes['onreset'] = %Script;
# the form was reset (FORM) 

attributes['onselect'] = %Script;
# some text was selected (INPUT, TEXTAREA) 

attributes['onsubmit'] = %Script;
# the form was submitted (FORM) 

attributes['onunload'] = %Script;
# all the frames have been removed (FRAMESET) 

attributes['onunload'] = %Script;
# the document has been removed (BODY) 

attributes['profile'] = %URI;
# named dictionary of meta info (HEAD) 

attributes['prompt'] = %Text;
# prompt message (ISINDEX) ; deprecated

attributes['readonly'] = RegExp(regexp=r'(readonly)')
#  (TEXTAREA) 

attributes['readonly'] = RegExp(regexp=r'(readonly)')
# for text and passwd (INPUT) 

attributes['rel'] = %LinkTypes;
# forward link types (A, LINK) 

attributes['rev'] = %LinkTypes;
# reverse link types (A, LINK) 

attributes['rows'] = %MultiLengths;
# list of lengths, default: 100% (1 row) (FRAMESET) 

attributes['rows'] = NUMBER#REQUIRED
#  (TEXTAREA) 

attributes['rowspan'] = NUMBER1
# number of rows spanned by cell (TD, TH) 

attributes['rules'] = %TRules;
# rulings between rows and cols (TABLE) 

attributes['scheme'] = CDATA
# select form of content (META) 

attributes['scope'] = %Scope;
# scope covered by header cells (TD, TH) 

attributes['scrolling'] = RegExp(regexp=r'(yes | no | auto)')auto
# scrollbar or none (FRAME, IFRAME) 

attributes['selected'] = RegExp(regexp=r'(selected)')
#  (OPTION) 

attributes['shape'] = %Shape;rect
# controls interpretation of coords (AREA) 

attributes['shape'] = %Shape;rect
# for use with client-side image maps (A) 

attributes['size'] = %Pixels;
#  (HR) ; deprecated

attributes['size'] = CDATA
# [+|-]nn e.g. size=+1, size=4 (FONT) ; deprecated

attributes['size'] = CDATA
# specific to each type of field (INPUT) 

attributes['size'] = CDATA#REQUIRED
# base font size for FONT elements (BASEFONT) ; deprecated

attributes['size'] = NUMBER
# rows visible (SELECT) 

attributes['span'] = NUMBER1
# COL attributes affect N columns (COL) 

attributes['span'] = NUMBER1
# default number of columns in group (COLGROUP) 

attributes['src'] = %URI;
# URI for an external script (SCRIPT) 

attributes['src'] = %URI;
# for fields with images (INPUT) 

attributes['src'] = %URI;
# source of frame content (FRAME, IFRAME) 

attributes['src'] = %URI;#REQUIRED
# URI of image to embed (IMG) 

attributes['standby'] = %Text;
# message to show while loading (OBJECT) 

attributes['start'] = NUMBER
# starting sequence number (OL) ; deprecated

attributes['style'] = %StyleSheet;
# associated style info (All elements but BASE, BASEFONT, HEAD, HTML, META, PARAM, SCRIPT, STYLE, TITLE) 

attributes['summary'] = %Text;
# purpose/structure for speech output (TABLE) 

attributes['tabindex'] = NUMBER
# position in tabbing order (A, AREA, BUTTON, INPUT, OBJECT, SELECT, TEXTAREA) 

attributes['target'] = %FrameTarget;
# render in this frame (A, AREA, BASE, FORM, LINK) 

attributes['text'] = %Color;
# document text color (BODY) ; deprecated

attributes['title'] = %Text;
# advisory title (All elements but BASE, BASEFONT, HEAD, HTML, META, PARAM, SCRIPT, TITLE) 

attributes['type'] = %ContentType;
# advisory content type (A, LINK) 

attributes['type'] = %ContentType;
# content type for data (OBJECT) 

attributes['type'] = %ContentType;
# content type for value when valuetype=ref (PARAM) 

attributes['type'] = %ContentType;#REQUIRED
# content type of script language (SCRIPT) 

attributes['type'] = %ContentType;#REQUIRED
# content type of style language (STYLE) 

attributes['type'] = %InputType;TEXT
# what kind of widget is needed (INPUT) 

attributes['type'] = %LIStyle;
# list item style (LI) ; deprecated

attributes['type'] = %OLStyle;
# numbering style (OL) ; deprecated

attributes['type'] = %ULStyle;
# bullet style (UL) ; deprecated

attributes['type'] = RegExp(regexp=r'(button | submit | reset)')submit
# for use as form button (BUTTON) 

attributes['usemap'] = %URI;
# use client-side image map (IMG, INPUT, OBJECT) 

attributes['valign'] = RegExp(regexp=r'(top | middle | bottom | baseline)')
# vertical alignment in cells (COL, COLGROUP, TBODY, TD, TFOOT, TH, THEAD, TR) 

attributes['value'] = CDATA
# Specify for radio buttons and checkboxes (INPUT) 

attributes['value'] = CDATA
# defaults to element content (OPTION) 

attributes['value'] = CDATA
# property value (PARAM) 

attributes['value'] = CDATA
# sent to server when submitted (BUTTON) 

attributes['value'] = NUMBER
# reset sequence number (LI) ; deprecated

attributes['valuetype'] = RegExp(regexp=r'(DATA | REF | OBJECT)')DATA
# How to interpret value (PARAM) 

attributes['version'] = CDATA%HTML.Version;
# Constant (HTML) ; deprecated

attributes['vlink'] = %Color;
# color of visited links (BODY) ; deprecated

attributes['vspace'] = %Pixels;
# vertical gutter (APPLET, IMG, OBJECT) ; deprecated

attributes['width'] = %Length;
#  (HR) ; deprecated

attributes['width'] = %Length;
# frame width (IFRAME) 

attributes['width'] = %Length;
# override width (IMG, OBJECT) 

attributes['width'] = %Length;
# table width (TABLE) 

attributes['width'] = %Length;
# width for cell (TD, TH) ; deprecated

attributes['width'] = %Length;#REQUIRED
# initial width (APPLET) ; deprecated

attributes['width'] = %MultiLength;
# column width specification (COL) 

attributes['width'] = %MultiLength;
# default width for enclosed COLs (COLGROUP) 

attributes['width'] = NUMBER
#  (PRE) ; deprecated

