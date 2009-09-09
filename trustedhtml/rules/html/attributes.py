"""
Index of Attributes
http://www.w3.org/TR/REC-html40/index/attributes.html
"""

attributes['abbr'] = text
# abbreviation for header cell

attributes['accept-charset'] = charsets
# list of supported charsets

attributes['accept'] = content_types
# list of MIME types for file upload

attributes['accesskey'] = character
# accessibility key character

attributes['action'] = uri_required
# server-side form handler

#attributes['align'] = %CAlign;
## relative to table; deprecated
#
#attributes['align'] = %IAlign;
## vertical or horizontal alignment; deprecated
#
#attributes['align'] = %LAlign;
## relative to fieldset; deprecated
#
#attributes['align'] = %TAlign;
## table position relative to window; deprecated
#
#attributes['align'] = (left | center | right)
## ; deprecated
#
#attributes['align'] = (left | center | right | justify)
## align, text alignment; deprecated
#
#attributes['align'] = (left | center | right | justify | char)
## 
#
#attributes['alink'] = %Color;
## color of selected links; deprecated
#
#attributes['alt'] = %Text;
## short description; deprecated
#
#attributes['alt'] = %Text;#REQUIRED
## short description
#
#attributes['alt'] = CDATA
## short description
#
#attributes['archive'] = CDATA
## comma-separated archive list; deprecated
#
#attributes['archive'] = CDATA
## space-separated list of URIs
#
#attributes['axis'] = CDATA
## comma-separated list of related headers
#
#attributes['background'] = %URI;
## texture tile for document background; deprecated
#
#attributes['bgcolor'] = %Color;
## background color for cells; deprecated
#
#attributes['bgcolor'] = %Color;
## background color for row; deprecated
#
#attributes['bgcolor'] = %Color;
## cell background color; deprecated
#
#attributes['bgcolor'] = %Color;
## document background color; deprecated
#
#attributes['border'] = %Pixels;
## controls frame width around table
#
#attributes['border'] = %Pixels;
## link border width; deprecated
#
#attributes['cellpadding'] = %Length;
## spacing within cells
#
#attributes['cellspacing'] = %Length;
## spacing between cells
#
#attributes['char'] = %Character;
## alignment char, e.g. char=':'
#
#attributes['charoff'] = %Length;
## offset for alignment char
#
#attributes['charset'] = %Charset;
## char encoding of linked resource
#
#attributes['checked'] = (checked)
## for radio buttons and check boxes
#
#attributes['cite'] = %URI;
## URI for source document or msg
#
#attributes['cite'] = %URI;
## info on reason for change
#
#attributes['class'] = CDATA
## space-separated list of classes
#
#attributes['classid'] = %URI;
## identifies an implementation
#
#attributes['clear'] = (left | all | right | none)none
## control of text flow; deprecated
#
#attributes['code'] = CDATA
## applet class file; deprecated
#
#attributes['codebase'] = %URI;
## base URI for classid, data, archive
#
#attributes['codebase'] = %URI;
## optional base URI for applet; deprecated
#
#attributes['codetype'] = %ContentType;
## content type for code
#
#attributes['color'] = %Color;
## text color; deprecated
#
#attributes['cols'] = %MultiLengths;
## list of lengths, default: 100% (1 col)
#
#attributes['cols'] = NUMBER#REQUIRED
## 
#
#attributes['colspan'] = NUMBER1
## number of cols spanned by cell
#
#attributes['compact'] = (compact)
## reduced interitem spacing; deprecated
#
#attributes['content'] = CDATA#REQUIRED
## associated information
#
#attributes['coords'] = %Coords;
## comma-separated list of lengths
#
#attributes['coords'] = %Coords;
## for use with client-side image maps
#
#attributes['data'] = %URI;
## reference to object's data
#
#attributes['datetime'] = %Datetime;
## date and time of change
#
#attributes['declare'] = (declare)
## declare but don't instantiate flag
#
#attributes['defer'] = (defer)
## UA may defer execution of script
#
#attributes['dir'] = (ltr | rtl)
## direction for weak/neutral text
#
#attributes['dir'] = (ltr | rtl)#REQUIRED
## directionality
#
#attributes['disabled'] = (disabled)
## unavailable in this context
#
#attributes['enctype'] = %ContentType;application/x-www- form-urlencoded
## 
#
#attributes['face'] = CDATA
## comma-separated list of font names; deprecated
#
#attributes['for'] = IDREF
## matches field ID value
#
#attributes['frame'] = %TFrame;
## which parts of frame to render
#
#attributes['frameborder'] = (1 | 0)1
## request frame borders?
#
#attributes['headers'] = IDREFS
## list of id's for header cells
#
#attributes['height'] = %Length;
## frame height
#
#attributes['height'] = %Length;
## height for cell; deprecated
#
#attributes['height'] = %Length;
## override height
#
#attributes['height'] = %Length;#REQUIRED
## initial height; deprecated
#
#attributes['href'] = %URI;
## URI for linked resource
#
#attributes['href'] = %URI;
## URI that acts as base URI
#
#attributes['hreflang'] = %LanguageCode;
## language code
#
#attributes['hspace'] = %Pixels;
## horizontal gutter; deprecated
#
#attributes['http-equiv'] = NAME
## HTTP response header name
#
#attributes['id'] = ID
## document-wide unique id
#
#attributes['ismap'] = (ismap)
## use server-side image map
#
#attributes['label'] = %Text;
## for use in hierarchical menus
#
#attributes['label'] = %Text;#REQUIRED
## for use in hierarchical menus
#
#attributes['lang'] = %LanguageCode;
## language code
#
#attributes['language'] = CDATA
## predefined script language name; deprecated
#
#attributes['link'] = %Color;
## color of links; deprecated
#
#attributes['longdesc'] = %URI;
## link to long description (complements alt)
#
#attributes['longdesc'] = %URI;
## link to long description (complements title)
#
#attributes['marginheight'] = %Pixels;
## margin height in pixels
#
#attributes['marginwidth'] = %Pixels;
## margin widths in pixels
#
#attributes['maxlength'] = NUMBER
## max chars for text fields
#
#attributes['media'] = %MediaDesc;
## designed for use with these media
#
#attributes['media'] = %MediaDesc;
## for rendering on these media
#
#attributes['method'] = (GET | POST)GET
## HTTP method used to submit the form
#
#attributes['multiple'] = (multiple)
## default is single selection
#
#attributes['name'] = CDATA
## 
#
#attributes['name'] = CDATA
## allows applets to find each other; deprecated
#
#attributes['name'] = CDATA
## field name
#
#attributes['name'] = CDATA
## name of form for scripting
#
#attributes['name'] = CDATA
## name of frame for targetting
#
#attributes['name'] = CDATA
## name of image for scripting
#
#attributes['name'] = CDATA
## named link end
#
#attributes['name'] = CDATA
## submit as part of form
#
#attributes['name'] = CDATA#REQUIRED
## for reference by usemap
#
#attributes['name'] = CDATA#REQUIRED
## property name
#
#attributes['name'] = NAME
## metainformation name
#
#attributes['nohref'] = (nohref)
## this region has no action
#
#attributes['noresize'] = (noresize)
## allow users to resize frames?
#
#attributes['noshade'] = (noshade)
## ; deprecated
#
#attributes['nowrap'] = (nowrap)
## suppress word wrap; deprecated
#
#attributes['object'] = CDATA
## serialized applet file; deprecated
#
#attributes['onblur'] = %Script;
## the element lost the focus
#
#attributes['onchange'] = %Script;
## the element value was changed
#
#attributes['onclick'] = %Script;
## a pointer button was clicked
#
#attributes['ondblclick'] = %Script;
## a pointer button was double clicked
#
#attributes['onfocus'] = %Script;
## the element got the focus
#
#attributes['onkeydown'] = %Script;
## a key was pressed down
#
#attributes['onkeypress'] = %Script;
## a key was pressed and released
#
#attributes['onkeyup'] = %Script;
## a key was released
#
#attributes['onload'] = %Script;
## all the frames have been loaded
#
#attributes['onload'] = %Script;
## the document has been loaded
#
#attributes['onmousedown'] = %Script;
## a pointer button was pressed down
#
#attributes['onmousemove'] = %Script;
## a pointer was moved within
#
#attributes['onmouseout'] = %Script;
## a pointer was moved away
#
#attributes['onmouseover'] = %Script;
## a pointer was moved onto
#
#attributes['onmouseup'] = %Script;
## a pointer button was released
#
#attributes['onreset'] = %Script;
## the form was reset
#
#attributes['onselect'] = %Script;
## some text was selected
#
#attributes['onsubmit'] = %Script;
## the form was submitted
#
#attributes['onunload'] = %Script;
## all the frames have been removed
#
#attributes['onunload'] = %Script;
## the document has been removed
#
#attributes['profile'] = %URI;
## named dictionary of meta info
#
#attributes['prompt'] = %Text;
## prompt message; deprecated
#
#attributes['readonly'] = (readonly)
## 
#
#attributes['readonly'] = (readonly)
## for text and passwd
#
#attributes['rel'] = %LinkTypes;
## forward link types
#
#attributes['rev'] = %LinkTypes;
## reverse link types
#
#attributes['rows'] = %MultiLengths;
## list of lengths, default: 100% (1 row)
#
#attributes['rows'] = NUMBER#REQUIRED
## 
#
#attributes['rowspan'] = NUMBER1
## number of rows spanned by cell
#
#attributes['rules'] = %TRules;
## rulings between rows and cols
#
#attributes['scheme'] = CDATA
## select form of content
#
#attributes['scope'] = %Scope;
## scope covered by header cells
#
#attributes['scrolling'] = (yes | no | auto)auto
## scrollbar or none
#
#attributes['selected'] = (selected)
## 
#
#attributes['shape'] = %Shape;rect
## controls interpretation of coords
#
#attributes['shape'] = %Shape;rect
## for use with client-side image maps
#
#attributes['size'] = %Pixels;
## ; deprecated
#
#attributes['size'] = CDATA
## [+|-]nn e.g. size=+1, size=4; deprecated
#
#attributes['size'] = CDATA
## specific to each type of field
#
#attributes['size'] = CDATA#REQUIRED
## base font size for FONT elements; deprecated
#
#attributes['size'] = NUMBER
## rows visible
#
#attributes['span'] = NUMBER1
## COL attributes affect N columns
#
#attributes['span'] = NUMBER1
## default number of columns in group
#
#attributes['src'] = %URI;
## URI for an external script
#
#attributes['src'] = %URI;
## for fields with images
#
#attributes['src'] = %URI;
## source of frame content
#
#attributes['src'] = %URI;#REQUIRED
## URI of image to embed
#
#attributes['standby'] = %Text;
## message to show while loading
#
#attributes['start'] = NUMBER
## starting sequence number; deprecated
#
#attributes['style'] = %StyleSheet;
## associated style info
#
#attributes['summary'] = %Text;
## purpose/structure for speech output
#
#attributes['tabindex'] = NUMBER
## position in tabbing order
#
#attributes['target'] = %FrameTarget;
## render in this frame
#
#attributes['text'] = %Color;
## document text color; deprecated
#
#attributes['title'] = %Text;
## advisory title
#
#attributes['type'] = %ContentType;
## advisory content type
#
#attributes['type'] = %ContentType;
## content type for data
#
#attributes['type'] = %ContentType;
## content type for value when valuetype=ref
#
#attributes['type'] = %ContentType;#REQUIRED
## content type of script language
#
#attributes['type'] = %ContentType;#REQUIRED
## content type of style language
#
#attributes['type'] = %InputType;TEXT
## what kind of widget is needed
#
#attributes['type'] = %LIStyle;
## list item style; deprecated
#
#attributes['type'] = %OLStyle;
## numbering style; deprecated
#
#attributes['type'] = %ULStyle;
## bullet style; deprecated
#
#attributes['type'] = (button | submit | reset)submit
## for use as form button
#
#attributes['usemap'] = %URI;
## use client-side image map
#
#attributes['valign'] = (top | middle | bottom | baseline)
## vertical alignment in cells
#
#attributes['value'] = CDATA
## Specify for radio buttons and checkboxes
#
#attributes['value'] = CDATA
## defaults to element content
#
#attributes['value'] = CDATA
## property value
#
#attributes['value'] = CDATA
## sent to server when submitted
#
#attributes['value'] = NUMBER
## reset sequence number; deprecated
#
#attributes['valuetype'] = (DATA | REF | OBJECT)DATA
## How to interpret value
#
#attributes['version'] = CDATA%HTML.Version;
## Constant; deprecated
#
#attributes['vlink'] = %Color;
## color of visited links; deprecated
#
#attributes['vspace'] = %Pixels;
## vertical gutter; deprecated
#
#attributes['width'] = %Length;
## ; deprecated
#
#attributes['width'] = %Length;
## frame width
#
#attributes['width'] = %Length;
## override width
#
#attributes['width'] = %Length;
## table width
#
#attributes['width'] = %Length;
## width for cell; deprecated
#
#attributes['width'] = %Length;#REQUIRED
## initial width; deprecated
#
#attributes['width'] = %MultiLength;
## column width specification
#
#attributes['width'] = %MultiLength;
## default width for enclosed COLs
#
#attributes['width'] = NUMBER
## ; deprecated

