"""
Content model definitions
http://www.w3.org/TR/REC-html40/sgml/loosedtd.html

Fix: add specification according to dtd:
http://www.w3.org/TR/REC-html40/sgml/dtd.html
"""

# Document text:
pcdata = [True]

# Element is empty:
empty = []

# Defined sets:
fontstyle = ['tt', 'i', 'b', 'u', 's', 'strike', 'big', 'small', ]
# Strict: ['tt', 'i', 'b', 'big', 'small', ]
phrase = ['em', 'strong', 'dfn', 'code', 'samp', 'kbd', 'var',
    'cite', 'abbr', 'acronym', ]
special = ['a', 'img', 'applet', 'object', 'font', 'basefont', 'br',
    'script', 'map', 'q', 'sub', 'sup', 'span', 'bdo', 'iframe', ]
# Strict: ['a', 'img',  'object', 'br', 'script', 'map', 'q', 'sub', 'sup', 'span', 'bdo', ]
formctrl = ['input', 'select', 'textarea', 'label', 'button']
inline = pcdata + fontstyle + phrase + special + formctrl
heading = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
list = ['ul', 'ol', 'dir', 'menu']
# Strict: ['ul', 'ol', ]
preformatted = ['pre']
block = heading + list + preformatted + ['p',
    'dl', 'div', 'center', 'noscript', 'noframes', 'blockquote',
    'form', 'isindex', 'hr', 'table', 'fieldset', 'address'] + \
    ['noindex'] # This not w3c tag, but it is used by Yandex search engine
# Strict: heading + list + preformatted + ['p',
#    'dl', 'div', 'noscript', 'blockquote',
#    'form', 'hr', 'table', 'fieldset', 'address']
flow = block + inline

def minus(lst, delta):
    return [item for item in lst if lst not in delta]

contents = {}
contents['a'] = minus(inline, ['a'])
contents['abbr'] = inline
contents['acronym'] = inline
contents['address'] = inline + ['p']
contents['applet'] = ['param'] + flow
contents['area'] = empty
contents['b'] = inline
contents['big'] = inline
contents['base'] = empty
contents['basefont'] = empty
contents['bdo'] = inline
contents['blockquote'] = flow # Strict: block + ['script'] 
contents['body'] = block + ['script'] + ['ins', 'del'] # Loose: flow + ['ins', 'del']
contents['br'] = empty
contents['button'] = minus(flow, formctrl + ['a', 'form', 'isindex', 'fieldset', 'iframe'])
contents['caption'] = inline
contents['center'] = flow
contents['cite'] = inline
contents['code'] = inline
contents['col'] = empty
contents['colgroup'] = ['col']
contents['dd'] = flow
contents['del'] = flow
contents['dfn'] = inline
contents['dir'] = ['li']
contents['div'] = flow
contents['dl'] = ['dt', 'dd']
contents['dt'] = inline
contents['em'] = inline
contents['fieldset'] = pcdata + ['legend'] + flow
contents['font'] = inline
contents['form'] = minus(flow, ['form'])
contents['frame'] = empty
contents['frameset'] = ['frameset', 'frame', 'noframes']
contents['h1'] = inline
contents['h2'] = inline
contents['h3'] = inline
contents['h4'] = inline
contents['h5'] = inline
contents['h6'] = inline
contents['head'] = ['title', 'isindex', 'base', 'script', 'style', 'meta', 'link', 'object']
contents['hr'] = empty
contents['html'] = ['head', 'body']
contents['i'] = inline
contents['iframe'] = flow
contents['img'] = empty
contents['input'] = empty
contents['ins'] = inline
contents['isindex'] = empty
contents['kbd'] = inline
contents['label'] = minus(inline, ['label'])
contents['legend'] = inline
contents['li'] = flow
contents['link'] = empty
contents['map'] = block + ['area']
contents['menu'] = ['li']
contents['meta'] = empty
contents['noframes'] = flow
contents['noscript'] = flow
contents['object'] = ['param'] + flow
contents['ol'] = ['li']
contents['optgroup'] = ['option']
contents['option'] = pcdata
contents['p'] = inline
contents['param'] = empty
contents['pre'] = minus(inline, ['img', 'object', 'applet', 'big', 'small', 'sub', 'sup', 'font', 'basefont']) 
contents['q'] = inline
contents['s'] = inline
contents['samp'] = inline
contents['script'] = pcdata # StyleSheet
contents['select'] = ['optgroup', 'option']
contents['small'] = inline
contents['span'] = inline
contents['strike'] = inline
contents['strong'] = inline
contents['style'] = pcdata # StyleSheet
contents['sub'] = inline
contents['sup'] = inline
contents['table'] = ['caption', 'col', 'colgroup' 'thead', 'tfoot', 'tbody']
contents['tbody'] = ['tr']
contents['td'] = flow
contents['textarea'] = pcdata
contents['tfoot'] = ['tr']
contents['th'] = flow
contents['thead'] = ['tr']
contents['title'] = pcdata
contents['tr'] = ['th', 'td']
contents['tt'] = inline
contents['u'] = inline
contents['ul'] = ['li']
contents['var'] = inline
contents['noindex'] = flow # This not w3c tag, but it is used by Yandex search engine
