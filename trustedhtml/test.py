# -*- coding: utf-8 -*-

def html_page(html):
    return """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
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

tiny_omg = u"""
<p><strong>q</strong><em>w</em><span style="text-decoration: underline;">e</span>r<span style="text-decoration: line-through;">t</span><sub>y</sub><sup>u</sup></p>
<ul>
<li>io</li>
</ul>
<ol>
<li>p[</li>
</ol>
<blockquote>
<blockquote><ol>
<li>]as</li>
</ol></blockquote>
</blockquote>
<ol>
<li>dfgh</li>
</ol>
<blockquote>
<p>jk</p>
</blockquote>
<p><a href="http://127.0.0.1:8000/editor/2/">zxc</a>v</p>
<p>b<a name="asdsa"></a>vnm1<a name="as"></a>2345sd</p>
<p><img style="float: left; border: 2px solid black; margin-top: 3px; margin-bottom: 3px; margin-left: 4px; margin-right: 4px;" src="/media/img/warning.png" alt="qwe" width="64" height="64" /></p>
<p>fs</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>fdf</p>
<table style="height: 50px;" border="3" cellspacing="2" cellpadding="1" width="100" frame="box" rules="cols" align="left" summary="asd">
<caption></caption> 
<tbody>
<tr>
<td>dd</td>
<td>fd</td>
</tr>
<tr>
<td omg='1'>fdf</td>
<td>fd</td>
</tr>
</tbody>
</table>
<p>df</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>n</p>
<table border="0" cellpadding="1">
<tbody>
<tr>
<td>122</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>3434</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td colspan="2">&nbsp;</td>
<td>567</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>89</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>&nbsp;</td>
<td rowspan="2">&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>00</td>
<td>&nbsp;</td>
</tr>
<tr>
<td><img title="Невинность" src="media/js/tiny_mce/plugins/emotions/img/smiley-innocent.gif" border="0" alt="Невинность" /></td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>ads</td>
</tr>
</tbody>
</table>
<p>n</p>
<address>a</address>
<pre>f<br /></pre>
<h1>1<br /></h1>
<h2>2</h2>
<h3>3</h3>
<h4>4</h4>
<h5>5</h5>
<h6>&clubs; 01.08.2008 &lt;img src="javascript:alert(1);"&gt; 16:27:31</h6>
"""

#    def v(self, value, catch=True):
#        if catch:
#            try:
#                return self.validate('name', 'attr', value)
#            except TrustedException, error:
#                return error
#        else:
#            return self.validate('name', 'attr', value)

#TrustedStr().v('')
#TrustedStr(allow_empty=False).v('')
#TrustedList(values=['leFt', 'right', ]).v('  lEft')
#TrustedList(values=['leFt', 'right', ], return_defined=False, case_sensitive=True).v('  lEft')
#TrustedList(values=['leFt', 'right', ], return_defined=False, case_sensitive=True).v('  leFt')
#TrustedUrl(allow_local=False).v('/gfdg')
#TrustedUrl(allow_local=False).v('gfdg')
#TrustedUrl().v('gfdg')
#TrustedUrl().v('/gfdg')
#TrustedUrl(allow_local=True).v('/gfdg')
#TrustedUrl(allow_local=True).v('gfdg')
#TrustedUrl(local_only=True).v('http://gfdg')
#TrustedNumber().v('')
#TrustedNumber(allow_sign=False).v('+34fd')
#TrustedNumber(allow_sign=False).v('34fd')
#TrustedNumber().v('-34fd')
#TrustedSize().v('+4 p xs')
#TrustedRules.border_width.v('thsin')
#TrustedRules.border_width.v('+3px')
#TrustedColor().v('deepskybluE   ')
#TrustedColor().v('rgb( 3,  343%,3)')
#TrustedColor().v('#fff')
#TrustedColor().v('#aaafff')
#TrustedColor().v('#aazfff')
#TrustedSequence(validator=TrustedNumber(), delimiter_char=',').v('a,23,,43,')
#TrustedStyle(trusted_list=[ {'text-decoration': TrustedList(values=['underline','line-through']),}, ]).v('text-decoration: line-through; foo: line-through; text-decoration: bar; text-decoration: underline')
#TrustedRules.border.v('')
#TrustedRules.border.v('2pxs')
#TrustedRules.border.v('soLid')
#TrustedRules.border.v('2pxs soLid')
#TrustedRules.border.v('blAck')
#TrustedRules.border.v('2pxs blAck')
#TrustedRules.border.v('soLid blAck')
#TrustedRules.border.v('2pxs soLid blAck')
#TrustedRules.border.v('pxs')
#TrustedRules.border.v('pxs soLid')
#TrustedRules.border.v('2pxs blAAck')
#TrustedRules.border.v('2pxs soLLid blAck')
#TrustedRules.style.v('float: left; margin: 4px; border: 2px solid black; ')
#TrustedHtml('<p><img style="float: left; border: 2px solid black; margin-top: 3px; margin-bottom: 3px; margin-left: 4px; margin-right: 4px;" src="/media/img/warning.png" alt="qwe" width="64" height="64" /></p>').html

#from utils.trustedhtml import *
