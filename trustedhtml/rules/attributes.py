# -*- coding: utf-8 -*-

from trustedhtml.classes import *
from trustedhtml.rules.common import *
from trustedhtml.rules import css

style = Style(attributes={
    'background': css.background,
    'background-color': css.background_color,
    'background-image': css.background_image,
    'background-repeat': css.background_repeat,
    'background-attachment': css.background_attachment,
    'background-position': css.background_position,
    
    'border': css.border_complex,
    'border-width': css.border_width,
    'border-style': css.border_style,
    'border-color': color,
    'border-collapse': css.border_collapse,
    
    'bottom': css.bottom,
    'clear': css.clear,
    'color': color,
    
    # content is big security hole
    #'content':
    #'counter-increment': 
    #'counter-reset': 
    
    'margin': css.margin,
    'margin-top': css.margin_top,

    'padding': css.padding,
    'padding-top': css.padding_top,

    'width': size,
    'height': size,

    'float': css.float,
}, equivalents = {
    'border': [
        'border-top', 'border-bottom', 'border-left', 'border-right'
    ],
    'border-width': [
        'border-top-width', 'border-bottom-width', 'border-left-width', 'border-right-width',
    ],
    'border-style': [
        'border-top-style', 'border-bottom-style', 'border-left-style', 'border-right-style',
    ],
    'border-color': [
        'border-top-color', 'border-bottom-color', 'border-left-color', 'border-right-color',
    ],
    'bottom': [
        'height', 'left', 'right', 'top', 'width',
    ],
    'letter-spacing': [
        'word-spacing',
    ],
    'page-break-after': [
        'page-break-before',
    ],
    'margin-top': [
        'margin-bottom', 'margin-left', 'margin-right',
    ],
    'max-height': [
        'max-width',
    ],
    'padding-top': [
        'padding-bottom', 'padding-left', 'padding-right',
    ],
})

link_type = List(values=[
    'alternate', 'stylesheet', 'start', 'next', 'prev', 
    'contents', 'index', 'glossary', 'copyright', 'chapter', 
    'section', 'subsection', 'appendix', 'help', 'bookmark',
] )

content_type = List(values=[
    'text/html', 'image/jpeg', 'image/png', 'image/gif', 'audio/mpeg', 'video/mpeg',    
    # Disabled: 'text/javascript', 'text/css', 
] ) # Full list: http://www.iana.org/assignments/media-types/

charset = List(values=[
    'utf-8', 'windows-1251', 'koi8-r', 'koi8-r', 'cp866', 'iso-8859-1', 'utf-16',
    # 'utf-7', # Disable (because of XSS)   
] ) # Full list: http://www.iana.org/assignments/character-sets

