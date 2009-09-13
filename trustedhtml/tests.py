# -*- coding: utf-8 -*-
#import rpdb2; rpdb2.start_embedded_debugger('1')

import re
import unittest
from trustedhtml.classes import *
from trustedhtml import rules
from trustedhtml import signals

class Classes(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_rule(self):
        rule = Rule()
        class Test(object):
            pass
        test = Test()
        self.assertEqual(rule.validate(test), test)

    def test_string(self):
        string = String()
        self.assertEqual(string.validate(''), '')
        self.assertEqual(string.validate('qwe'), 'qwe')
        self.assertEqual(string.validate('  qw e '), 'qw e')
        
    def test_list(self):
        rule = List(values=['a', 'aB', ], strip=True)
        self.assertRaises(IncorrectException, rule.validate, 'ac')
        self.assertEqual(rule.validate('  a '), 'a')
        self.assertEqual(rule.validate('  Ab '), 'aB')
        
    def test_list_case(self):
        rule = List(values=['a', 'aB', ], return_defined=False, case_sensitive=True)
        self.assertRaises(IncorrectException, rule.validate, 'ac')
        self.assertEqual(rule.validate('  a '), 'a')
        self.assertRaises(IncorrectException, rule.validate, '  Ab ')

    def test_regexp_regexp(self):
        rule = RegExp(regexp=r'@*([-+]?\d{1,7})@*$')
        self.assertRaises(IncorrectException, rule.validate, '-')
        self.assertRaises(IncorrectException, rule.validate, '@@@-')
        self.assertEqual(rule.validate('  @@@-12@ '), '-12')
        
    def test_regexp_expand(self):
        rule = RegExp(regexp=r'([-+]?\d*),(?P<a>\d*)$', expand=r'\g<a>;\1')
        self.assertEqual(rule.validate('-12,34'), '34;-12')
        self.assertRaises(IncorrectException, rule.validate, '-12,34a')
        
    def test_uri_core(self):
        rule = Uri()
        self.assertEqual(rule.preprocess('Q%WW%R%1TT%2%YYY%%34UU%a5%6A', None), u'Q%25WW%25R%251TT%252%25YYY%25%34UU%a5%6A')
        uri = 'http://www.ics.uci.edu/pub/ietf/uri/?arg1=value1&arg2=value2#Related'
        self.assertEqual(rule.split(uri),
            ('http', 'www.ics.uci.edu', '/pub/ietf/uri/', 'arg1=value1&arg2=value2', 'Related'))
        self.assertEqual(rule.split('http:/www.ics.uci.edu/'),
            ('http', None, '/www.ics.uci.edu/', None, None))
        self.assertEqual(rule.split('http:www.ics.uci.edu/'),
            ('http', None, 'www.ics.uci.edu/', None, None))
        self.assertEqual(rule.split('http/://www.ics.uci.edu/'),
            (None, None, 'http/://www.ics.uci.edu/', None, None))
        self.assertEqual(rule.build(*rule.split(uri)), uri)

    def test_uri_a(self):
        rule = Uri()
        self.assertRaises(IncorrectException, rule.validate, 'script:alert("hack")')
        self.assertEqual(rule.validate('http://foreign.com/img.jpg'), 'http://foreign.com/img.jpg')
        self.assertEqual(rule.validate('http://local.com/img.jpg'), 'http://local.com/img.jpg')
        self.assertEqual(rule.validate('ftp://local.com/img.jpg'), 'ftp://local.com/img.jpg')
        self.assertEqual(rule.validate('http://local-mirror.com/img.jpg'), 'http://local-mirror.com/img.jpg')
        self.assertEqual(rule.validate('/img.jpg'), '/img.jpg')
        self.assertEqual(rule.validate('img.jpg'), 'img.jpg')

    def test_uri_a_local(self):
        rule = Uri(local_sites=['local.com', 'local-mirror.com'])
        self.assertRaises(IncorrectException, rule.validate, 'script:alert("hack")')
        self.assertEqual(rule.validate('http://foreign.com/img.jpg'), 'http://foreign.com/img.jpg')
        self.assertEqual(rule.validate('http://local.com/img.jpg'), '/img.jpg')
        self.assertEqual(rule.validate('ftp://local.com/img.jpg'), 'ftp://local.com/img.jpg')
        self.assertEqual(rule.validate('http://local-mirror.com/img.jpg'), '/img.jpg')
        self.assertEqual(rule.validate('/img.jpg'), '/img.jpg')
        self.assertEqual(rule.validate('img.jpg'), 'img.jpg')
            
    def test_uri_img(self):
        rule = Uri(allow_sites=['local.com', 'local-mirror.com'])
        self.assertRaises(IncorrectException, rule.validate, 'script:alert("hack")')
        self.assertRaises(IncorrectException, rule.validate, 'http://foreign.com/img.jpg')
        self.assertEqual(rule.validate('http://local.com/img.jpg'), 'http://local.com/img.jpg')
        self.assertEqual(rule.validate('ftp://local.com/img.jpg'), 'ftp://local.com/img.jpg')
        self.assertEqual(rule.validate('http://local-mirror.com/img.jpg'), 'http://local-mirror.com/img.jpg')
        self.assertEqual(rule.validate('/img.jpg'), '/img.jpg')
        self.assertEqual(rule.validate('img.jpg'), 'img.jpg')
            
    def test_uri_img_local(self):
        rule = Uri(allow_sites=['local.com', 'local-mirror.com'], local_sites=['local.com', 'local-mirror.com'])
        self.assertRaises(IncorrectException, rule.validate, 'script:alert("hack")')
        self.assertRaises(IncorrectException, rule.validate, 'http://foreign.com/img.jpg')
        self.assertEqual(rule.validate('http://local.com/img.jpg'), '/img.jpg')
        self.assertEqual(rule.validate('ftp://local.com/img.jpg'), 'ftp://local.com/img.jpg')
        self.assertEqual(rule.validate('http://local-mirror.com/img.jpg'), '/img.jpg')
        self.assertEqual(rule.validate('/img.jpg'), '/img.jpg')
        self.assertEqual(rule.validate('img.jpg'), 'img.jpg')

    def test_uri_ext(self):
        rule = Uri(allow_sites=['local.com', 'local-mirror.com'], local_sites=['local.com', 'local-mirror.com'])
        self.assertEqual(rule.validate('http://local.com?qw'), '?qw')
        self.assertEqual(rule.validate('http://local.com'), '/')

    def test_or(self):
        rule = Or(rules=[
            List(values=['a', 'aB', ]),
            RegExp(regexp=r'([-+]?\d{1,7})$'),
        ])
        self.assertRaises(IncorrectException, rule.validate, '')
        self.assertRaises(IncorrectException, rule.validate, '-')
        self.assertEqual(rule.validate('  -12 '), '-12')
        self.assertEqual(rule.validate('  Ab '), 'aB')
        
    def test_or_empty(self):
        rule = Or(rules=[
            List(values=['a', 'aB', ]),
            RegExp(regexp=r'([-+]?\d{1,7})$', allow_empty=False),
        ])
        self.assertRaises(EmptyException, rule.validate, '')
        self.assertRaises(IncorrectException, rule.validate, '-')
        self.assertEqual(rule.validate('  -12 '), '-12')
        self.assertEqual(rule.validate('  Ab '), 'aB')

    def test_and(self):
        rule = And(rules=[
            RegExp(regexp=r'!*(\w{2})$'),
            List(values=['a', 'aB', 'Cd', ]),
        ])
        self.assertRaises(IncorrectException, rule.validate, '')
        self.assertRaises(IncorrectException, rule.validate, '-')
        self.assertRaises(IncorrectException, rule.validate, 'a')
        self.assertEqual(rule.validate('  Ab '), 'aB')
        self.assertRaises(IncorrectException, rule.validate, 'ef')
        self.assertEqual(rule.validate('  !!cD '), 'Cd')

    def test_style(self):
        text_decoration = List(values=['underline', 'line-through'], )
        simple_margin_top = RegExp(regexp=r'(\w+)$')
        rule = Style(rules={
            'text-decoration': text_decoration,
            'margin-top': simple_margin_top,
        }, )
        self.assertEqual(
            rule.validate(
                'text-decoration: line-through; foo: line-through;'
                'text-decoration: bar; text-decoration: underline;'
                'margin-ttop: 1; margin-tOP: 3;'
            ),
            'text-decoration: underline; margin-top: 3;'
        )

    def tearDown(self):
        pass
    
class Css(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_re(self):
        self.assertEqual(re.match('%(escape)s$' % rules.css.grammar.grammar, '\\\a'), None)
        self.assertNotEqual(re.match('%(escape)s$' % rules.css.grammar.grammar, u'\\\u044f'), None)
        self.assertEqual(re.match('%(string1)s$' % rules.css.grammar.grammar, '"img".jpg"'), None)
        self.assertNotEqual(re.match('%(string1)s$' % rules.css.grammar.grammar, '"img\\".jpg"'), None)

    def test_number(self):
        self.assertRaises(IncorrectException, rules.css.syndata.number.validate, 'a')
        self.assertRaises(IncorrectException, rules.css.syndata.number.validate, '1.')
        self.assertEqual(rules.css.syndata.number.validate('  12.3 '), '12.3')

    def test_length(self):
        self.assertRaises(IncorrectException, rules.css.syndata.length.validate, '-')
        self.assertRaises(IncorrectException, rules.css.syndata.length.validate, '-12pxs')
        self.assertRaises(IncorrectException, rules.css.syndata.length.validate, '-12')
        self.assertEqual(rules.css.syndata.length.validate('  -12.3px '), '-12.3px')
        self.assertEqual(rules.css.syndata.length.validate('  0 '), '0')

    def test_color(self):
        self.assertEqual(rules.css.syndata.color.validate('  WinDow '), 'window')
        self.assertEqual(rules.css.syndata.color.validate('Red'), 'red')
        self.assertEqual(rules.css.syndata.color.validate('rgb( 1,  34%,5)'), 'rgb(1,34%,5)')
        self.assertEqual(rules.css.syndata.color.validate('rgba( 1,  34%,5  , 1 )'), 'rgba(1,34%,5,1)')
        self.assertEqual(rules.css.syndata.color.validate('rgb( 1,  34%,-5)'), 'rgb(1,34%,-5)')
        self.assertRaises(IncorrectException, rules.css.syndata.color.validate, 'rgb( 1,  34%,5a)')
        self.assertRaises(IncorrectException, rules.css.syndata.color.validate, 'rgb( 1,  34%,5)-')
        self.assertRaises(IncorrectException, rules.css.syndata.color.validate, 'rgb( 1,  34%,0.5)')
        self.assertEqual(rules.css.syndata.color.validate('#fff'), '#fff')
        self.assertEqual(rules.css.syndata.color.validate('#aaafff'), '#aaafff')
        self.assertRaises(IncorrectException, rules.css.syndata.color.validate, '#aazfff')
        
    def test_uri(self):
        self.assertEqual(rules.css.syndata.uri.validate('url( img.jpg  )'), 'url(img.jpg)')
        self.assertEqual(rules.css.syndata.uri.validate('url( http://ya.ru/img.jpg   )'), 'url(http://ya.ru/img.jpg)')
        self.assertEqual(rules.css.syndata.uri.validate(u'url( http://ya.ru/im\u044fg.jpg  )'), u'url(http://ya.ru/im\u044fg.jpg)')
        self.assertEqual(rules.css.syndata.uri.validate('url( http://ya.ru/img.jpg \t   )'), 'url(http://ya.ru/img.jpg)')
        self.assertRaises(IncorrectException, rules.css.syndata.uri.validate, 'url( script:alert(1)  )')
        self.assertEqual(rules.css.syndata.uri.validate('url( \"http://ya.ru/img\' .jpg\"  )'), 'url(\"http://ya.ru/img\' .jpg\")')
        self.assertEqual(rules.css.syndata.uri.validate('url( \'http://ya.ru/img\" .jpg\'  )'), 'url(\'http://ya.ru/img\" .jpg\')')
        self.assertEqual(rules.css.syndata.uri.validate('url( \'http://ya.ru/img\\\' .jpg\'  )'), 'url(\'http://ya.ru/img\\\' .jpg\')')

    def test_border(self):
        self.assertEqual(rules.css.box.border.validate(' 2px  Solid Black'), '2px solid black')
        self.assertEqual(rules.css.box.border.validate(' 2px  Black'), '2px black')
        self.assertEqual(rules.css.box.border.validate(' 2px  Solid Black'), '2px solid black')
        self.assertEqual(rules.css.box.border.validate(' 2px  Solid'), '2px solid')
        self.assertEqual(rules.css.box.border.validate(' Solid Black'), 'solid black')
        self.assertEqual(rules.css.box.border.validate(' Solid'), 'solid')
        self.assertEqual(rules.css.box.border.validate(' Black'), 'black')
        self.assertEqual(rules.css.box.border.validate(' 2px'), '2px')
        self.assertRaises(IncorrectException, rules.css.box.border.validate, ' 2px  Solid BBlack')
        self.assertRaises(IncorrectException, rules.css.box.border.validate, ' 2px  SSolid Black')
        self.assertRaises(IncorrectException, rules.css.box.border.validate, ' 2pxx  Solid Black')
        self.assertRaises(IncorrectException, rules.css.box.border.validate, ' 2px  Black  Solid')
        self.assertRaises(IncorrectException, rules.css.box.border.validate, ' Solid Black 2px')
        self.assertRaises(IncorrectException, rules.css.box.border.validate, ' 2px Solid Black 2px')
        self.assertRaises(IncorrectException, rules.css.box.border.validate, ' 2px 2px Solid Black')
        self.assertRaises(IncorrectException, rules.css.box.border.validate, ' 2px Solid Black Black')
        self.assertRaises(IncorrectException, rules.css.box.border.validate, '')

    def test_background_position(self):
        self.assertEqual(rules.css.colors.background_position.validate(' lEft  toP '), 'left top')
        self.assertRaises(IncorrectException, rules.css.colors.background_position.validate, ' toP  lEft ')
        self.assertEqual(rules.css.colors.background_position.validate(' lEft  12pX '), 'left 12pX')
        self.assertRaises(IncorrectException, rules.css.colors.background_position.validate, ' lEft 12 px ')
        self.assertRaises(IncorrectException, rules.css.colors.background_position.validate, ' lEft 12pxs ')
        self.assertRaises(IncorrectException, rules.css.colors.background_position.validate, ' toP 12pX ')
        self.assertEqual(rules.css.colors.background_position.validate(' 34em  toP '), '34em top')
        self.assertRaises(IncorrectException, rules.css.colors.background_position.validate, ' 34em lEft ')
        self.assertEqual(rules.css.colors.background_position.validate(' 34em  12px '), '34em 12px')
        self.assertEqual(rules.css.colors.background_position.validate(' 34em  '), '34em')
        self.assertEqual(rules.css.colors.background_position.validate(' lEft  '), 'left')
        self.assertEqual(rules.css.colors.background_position.validate(' toP  '), 'top')
        self.assertRaises(IncorrectException, rules.css.colors.background_position.validate, '')

    def test_background(self):
        self.assertEqual(rules.css.colors.background.validate(' rEd repEat   sCroll'), 'red repeat scroll')
        self.assertEqual(rules.css.colors.background.validate(' rgb(10%,100,255) rEpeat sCroll lEft'), 'rgb(10%,100,255) repeat scroll left')
        self.assertEqual(rules.css.colors.background.validate('#FFFFFF none repeat scroll 0'), '#FFFFFF none repeat scroll 0')
#        self.assertEqual(rules.css.colors.background.validate('#FFFFFF none repeat scroll 0 0'), '#FFFFFF none repeat scroll 0 0')

    def test_full(self):
        self.assertEqual(rules.css.full.validate(
            'color:black;font-family:sans-serif;'), 
            'color: black; font-family: sans-serif;')
        self.assertEqual(rules.css.full.validate(
            'background:#FDFEFF url(/media/img/header.gif) repeat-x scroll center;'
            'height:auto; margin:0; padding:2; ppading: 2px; width:auto;'),
            'background: #FDFEFF url(/media/img/header.gif) repeat-x scroll center; height: auto; margin: 0; width: auto;')
        
    def test_custom(self):
        lst = rules.css.custom.disabled + rules.css.custom.for_table + \
            rules.css.custom.for_image + rules.css.custom.for_table_and_image + \
            rules.css.custom.allowed
        append = []
        remove = [name for name in rules.css.values.values.iterkeys()]
        for item in lst:
            self.assertFalse(item in append)
            append.append(item)
            self.assertTrue(item in remove)
            remove.remove(item)
        self.assertFalse(remove)

    def tearDown(self):
        pass

    
class Html(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_values(self):
#        values['charset'],
#        values['coords'],
#        values['rel'],
#        values['rev'],
#        values['shape'],
#        values['tabindex'],
#        values['target'],
#        values['type'],
#        values['shape'],
#        values['width~c'],
#        values['accept'],
#        values['accept-charset'],
#        values['enctype'],
#        values['method'],
#        values['frameborder'],
#        values['marginheight'],
#        values['marginwidth'],
#        values['scrolling'],
#        values['cols'],
#        values['rows'],
#        values['profile'],
#        values['version'],
#        values['longdesc'],
#        values['for'],
#        values['media'],
#        values['archive'],
#        values['axis'],
#        values['headers'],
#        values['scope'],
        pass

    def test_custom(self):
        lst = rules.html.attributes.disabled + rules.css.attributes.for_table + \
            rules.css.custom.for_image + rules.css.custom.for_table_and_image + \
            rules.css.custom.allowed
        append = []
        remove = [name for name in rules.css.values.values.iterkeys()]
        for item in lst:
            self.assertFalse(item in append)
            append.append(item)
            self.assertTrue(item in remove)
            remove.remove(item)
        self.assertFalse(remove)
    
    def test_html(self):
        self.assertEqual(rules.html.full.validate(
            '<p>test</p>'),
            '<p>test</p>')
        self.assertEqual(rules.html.full.validate(
            '<p foo="bar">test</p>'),
            '<p>test</p>')
        self.assertEqual(rules.html.full.validate(
            '<p>te<foo></foo>st</p>'),
            '<p>test</p>')
        self.assertEqual(rules.html.full.validate(
            '<p>t<foo>es</foo>t</p>'),
            '<p>tt</p>')
        self.assertEqual(rules.html.full.validate(
            '<p>   t   <span>   e   </span>   <span>   s   </span>   t   </p>'), 
            '<p> t <span> e </span> <span> s </span> t </p>')
        self.assertEqual(rules.html.full.validate(
            '<p>   te   <span></span>   <span>   s   </span>   t   </p>'), 
            '<p> te <span> s </span> t </p>')
        self.assertEqual(rules.html.full.validate(
            '<p> te<span> </span> <span> </span> st </p>'), 
            '<p> te st </p>')
        self.assertEqual(rules.html.full.validate(
            ' te<span> </span> <span> </span> st '), 
            '<p>te st</p>')
        self.assertEqual(rules.html.full.validate(
            '<p><img style="float: left; border: 2px solid black; margin-top: 3px; margin-bottom: 3px; margin-left: 4px; margin-right: 4px;" src="/media/img/warning.png" alt="qwe" width="64" height="64" /></p>'),
            '<p><img style="float: left; border: 2px solid black; margin-top: 3px; margin-bottom: 3px; margin-left: 4px; margin-right: 4px;" src="/media/img/warning.png" alt="qwe" width="64" height="64" /></p>')

    def tearDown(self):
        pass
    
    
class Signals(unittest.TestCase):
    def setUp(self):
        def done(sender, **kwargs):
            pass

        def exception(sender, **kwargs):
            pass

        signals.rule_done.connect(done)        
        signals.rule_exception.connect(exception)        

    def tearDown(self):
        pass


def get_html(html):
    return """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>For w3c</title>
    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
    <meta http-equiv="Content-Language" content="ru" />
</head>
<body>
%s
</body>
</html>
""" % html

magic_hack_37 = '<p>-<i\0mg src="1.jpg">' + r'''
0&#x26x26&#38#38+&#x26;x26;&#38;#38;
1<IMG SRC='&#106&#0000097asdasd'>
2<IMG SRC="javascript:alert('XSS');">
3<IMG SRC=JaVaScRiPt:alert('XSS')>
4<IMG """><SCRIPT>alert("XSS")</SCRIPT>">
5<img src=&#106;&#97;&#118;&#97;&#115;&#99;&#114;&#105;&#112;&#116;&#58;&#97;&#108;&#101;&#114;&#116;&#40;&#39;&#88;&#83;&#83;&#39;&#41;>
6<IMG SRC=&#0000106&#0000097&#0000118&#0000097&#0000115&#0000099&#0000114&#0000105&#0000112&#0000116&#0000058&#0000097&#0000108&#0000101&#0000114&#0000116&#0000040&#0000039&#0000088&#0000083&#0000083&#0000039&#0000041>
7<IMG SRC=&#x6A&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x70&#x74&#x3A&#x61&#x6C&#x65&#x72&#x74&#x28&#x27&#x58&#x53&#x53&#x27&#x29>
8<A href="&#x6A&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x70&#x74&#x3A&#x61&#x6C&#x65&#x72&#x74&#x28&#x27&#x58&#x53&#x53&#x27&#x29">a</A>
9<A href=%6A%61%76%61%73%63%72%69%70%74%3A%61%6C%65%72%74%28%27%58%53%53%27%29>a</A>
A<IMG SRC="jav   ascript:alert('XSS');">
B<SCRIPT/XSS SRC="http://ha.ckers.org/xss.js"></SCRIPT>
C<SCRIPT SRC=http://ha.ckers.org/xss.js?<B></SCRIPT>
D<SCRIPT SRC=//ha.ckers.org/.j></SCRIPT>
E<IMG SRC="javascript:alert('XSS')" <IMG SRC="1.jpg">
F<BODY ONLOAD=alert('XSS')>BODY</BODY>
G<IMG SRC='vbscript:msgbox("XSS")'>
H<img style="xss:expr/*XSS*/ession(alert('XSS'))">
I<!--[if gte IE 4]><SCRIPT>alert('XSS');</SCRIPT><![endif]-->
J<A HREF="h
tt''' + '\0' + r'''p://6&#9;6.000146.0x7.147/">XSS</A>
K<IMG STYLE="exp/*<A STYLE='no\xss:noxss("*//*");xss:&#101;x&#x2F;*XSS*//*/*/pression(alert("XSS"))'>a</a>
L<A HREF="http://%77%77%77%2E%67%6F%6F%67%6C%65%2E%63%6F%6D">XSS</A>
M<DIV STYLE="background-image: url(&#1;javascript:alert('XSS'))">div</div>
N<DIV STYLE="background:#fff url(\0031.jpg);">NOXSS</div>
O<DIV STYLE="background-image:url(javascript\3aalert(1))">XSS</DIV>
O<DIV STYLE="background-image:\0075\0072\006C\0028'\006a\0061\0076\0061\0073\0063\0072\0069\0070\0074\003a\0061\006c\0065\0072\0074\0028'\0058'\0029'\0029">XSS</DIV>
P<IMG SRC='%399.jpg'>
Q<DIV STYLE="background-image:url('\x3c\x3C\u003c\u003C')>div</div>
R<A HREF='%uff1cscript%uff1ealert("XSS")%uff1c/script%uff1e'>asd</A>
S<DIV sstyle=foobar"tstyle="foobar"ystyle="foobar"lstyle="foobar"estyle="foobar"=-moz-binding:url(http://h4k.in/mozxss.xml#xss)>foobar#xss)" a=">asd"</DIV>
T<IMG SRC='vbscript:Execute(MsgBox(chr(88)&chr(83)&chr(83)))'>
U<A HREF='res://c:\\program%20files\\adobe\\acrobat%207.0\\acrobat\\acrobat.dll/#2/#210'>asd</A>
V<A onclick=eval/**/(/ale/.source%2b/rt/.source%2b/(7)/.source);>asd</A>
W<!--adasda<IMG SRC='1.jpg'> ->1w<!- adasda IMG SRC='1.jpg'>2w-->3w->4w> 
X<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN" "http://www.w3.org/TR/REC-html40/transitional.dtd">
Y<B attr='foo'>y1</b>,<b>y2</B><B Foo='bar'>y3</b><B Foob='bar'>y4</b>
Z<html>foo<!bar</html>text
</p>'''

def replace(value):
    value = value.replace('\n', ' ')
    value = value.replace('\r', ' ')
    value = value.replace('</p>', '</p>\n')
    return value

tinymce=u"""
<p>q<strong>w</strong>e<em>r</em>t<span style="text-decoration: underline;">y</span>u<span style="text-decoration: line-through;">i</span>o<span style="text-decoration: line-through;"><span style="text-decoration: underline;"><em><strong>p</strong></em></span></span>[]a<sub>s</sub>d<sup>f</sup>g&amp;hjkl;'</p>
<p><a name="ANC"></a>a</p>
<ul>
<li>b
<ul>
<li>A</li>
<li>B</li>
<li>C</li>
</ul>
</li>
<li>c</li>
<li>d</li>
</ul>
<ol>
<li>1<ol>
<li>!</li>
<li>@</li>
<li>#</li>
</ol></li>
<li>2</li>
<li>3</li>
</ol><address>H</address>
<pre>
J
JJJJ
JJ
</pre>
<h1>1</h1>
<h2>2</h2>
<h3>3</h3>
<h4>4</h4>
<h5>5</h5>
<h6>6</h6>
<p><a href="http://ya.ru">Z</a>X<a href="/news" target="_blank">C</a>V<a href="#ANC">B</a>NM<img title="sb" src="/media/img/search.jpg" alt="Search button" width="30" height="30" />&lt;</p>
<p><img id="I1" style="border: 1px solid black; margin: 2px 3px; float: right;" src="/media/img/logo.png" alt="" width="94" height="94" /></p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>And</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>this:</p>
<p>&nbsp;</p>
<p>
<object width="100" height="100" data="http://www.youtube.com/watch?v=rAy8JbMitog" type="application/x-shockwave-flash">
<param name="src" value="http://www.youtube.com/watch?v=rAy8JbMitog" />
</object>
</p>
<p>Options:</p>
<p>
<object width="425" height="350" data="http://www.youtube.com/v/rAy8JbMitog" type="application/x-shockwave-flash">
<param name="loop" value="false" />
<param name="src" value="http://www.youtube.com/v/rAy8JbMitog" />
<param name="align" value="right" />
<param name="bgcolor" value="#a1f074" />
<param name="vspace" value="10" />
<param name="hspace" value="30" />
</object>
</p>
<p>&nbsp;</p>
<p>&amp;&euro;&delta;&nbsp;&Theta;</p>
<blockquote>
<p>asdas</p>
</blockquote>
<p><del>b</del><ins>c</ins>d<del>e</del>f</p>
<table border="0">
<tbody>
<tr>
<td>qq</td>
<td colspan="2">
<p>wwweeee</p>
</td>
</tr>
<tr>
<td>aaaa</td>
<td>ss</td>
<td>ddd</td>
</tr>
</tbody>
</table>
<table style="border-color: #37c5c7; border-width: 2px; height: 200px; background-color: #bacbb8; width: 100%;" border="2" cellspacing="3" cellpadding="2" frame="hsides" rules="rows">
<caption></caption>
<tbody>
<tr style="background-image: url(/media/img/content-corner.gif);" align="right">
<td>ad</td>
<td>qw</td>
<td>
<table style="height: 100px;" width="40" frame="lhs" rules="cols" align="left" summary="asd" hack='on'>
<caption></caption> 
<tbody>
<tr>
<td>dd</td>
<td>fd</td>
</tr>
<tr>
<td>fdf</td>
<td>fd</td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td></td>
<td style="background-color: #a2a1c4;" colspan="2" rowspan="2" align="center" valign="top">big</td>
</tr>
<tr>
<td>zx</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<p>&lt;img src="javascript:alert(1);"&gt;</p>
<p>русский<br />end</p>
"""        
