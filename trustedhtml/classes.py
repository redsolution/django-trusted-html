# -*- coding: utf-8 -*-

import re
import copy
from beautifulsoup import BeautifulSoup, NavigableString, Tag
from django.contrib.sites.models import Site
from django.utils.encoding import iri_to_uri
from django.dispatch import Signal

from signals import *

TRUSTED_PREPARINGS = 2
TRUSTED_ITERATIONS = 2
TRUSTED_QUITE = False

class TrustedException(ValueError):
    u"""
    Base trustedhtml exception.
    """
    pass

class EmptyException(TrustedException):
    u"""
    Raised when value is empty and ``allow_empty`` flag is False.
    
    This exception means that attribute must be removed. 
    """
    pass
 
class IncorrectException(TrustedException):
    u"""
    Raised when value is incorrect. 
    
    This exception means that attribute must be removed. 
    """
    pass
 
class RequiredException(TrustedException):
    u"""
    Raised when value is empty and ``required`` flag is True.
    
    This exception means that hole tag must be removed.
    """
    pass
 
class InvalidException(TrustedException):
    u"""
    Raised when value pass check and invalid flag is True.
    
    This exception means that hole tag must be removed.
    """
    pass
    
class SequenceException(TrustedException):
    u"""
    Raised when element not corresponded to sequence. 
    
    Example: color is not specified for "border" style property
    """
    pass
 
class Tag(object):
    u"""Used when we need tags like in beautifulsoup"""
    def __init__(self, name='', attrs=[]):
        self.name = name
        self.attrs = attrs
    
class Run(object):
    u"""
    
    """
    def __init__(self, trusted_list, data=None, equivalents={}):
        self.trusted_list = trusted_list
        self.data = data
        self.equivalents = equivalents
    
    def check(self, tag):
        if not self.trusted_list:
            tag.attrs = [] 
            return True
        try:
            for index, trusted in enumerate(self.trusted_list):
                quite = index < len(self.trusted_list) - 1
                try:
                    correct = {}
                    dictionary = dict(tag.attrs)
                    for main, validator in trusted.iteritems():
                        attributes = [main]
                        attributes += self.equivalents.get(main, [])
                        for attribute in attributes:
                            if attribute in dictionary:
                                value = dictionary[attribute] 
                            else:
                                value = None
                            try:
                                correct[attribute] = validator.validate(tag.name, attribute, value, 
                                    path=self, data=self.data, quite=quite)
                            except EmptyException:
                                pass
                    order = [attr for attr, value in tag.attrs]
                    other = [attr for attr, value in correct.iteritems() if attr not in order]
                    order.extend(other)
                    sequence = [(order.index(attr), attr, value) for attr, value in correct.iteritems()]
                    sequence.sort()
                    tag.attrs = [(item, value) for index, item, value in sequence]
                    return True
                except RequiredException:
                    continue
        except InvalidException:
            return None
        return False

class Rule(object):
    u"""
    Base rule class.
    All rules inherit it and overwrite ``core`` or ``__init__`` functions.
    """

    def __init__(self, required=False, default=None, allow_empty=True,
        invalid=False, strip=True, data=None, **kwargs):
        u"""
        Sets behaviour for the rule:

        ``required`` if True than value is required.
        Example: attribute "src" for tag "img".

        ``default`` if is not None and validation fail than will return this one.
        Example: attribute "alt" for tag "img". 

        ``allow_empty`` if True than value can be empty.
        Example: attribute "width" for tag "img".

        ``invalid`` if True than result of validation will be inverted.
        Example: "none" value for "display" style property
        (we want to remove such tag).

        ``strip`` if True than remove leading and trailing whitespace.

        ``data`` any extended data, usually used by signals.
        """
        self.required = required
        if default is not None:
            default = unicode(default)
        self.default = default
        self.allow_empty = allow_empty
        self.invalid = invalid
        self.strip = strip
        self.data = data


    def validate(self, value, path=[]):
        u"""
        Main interface function. Call it to validate specified ``value``.
        
        Returns correct value or raise exception.
        
        ``path`` is the list from rules that called this validation.
        First element of this list will be first rule.
        
        This function will call ``core()`` that can be overwritten by subclasses.
        """
        try:
            try:
                if not self.allow_empty and not value:
                    raise EmptyException
                if value is None:
                    value = ''
                value = unicode(value)
                if self.strip:
                    value = value.strip()
                value = self.core(value, path)
                value = unicode(value)
                if not self.allow_empty and not value:
                    raise EmptyException
            except TrustedException, exception:
                if self.default is None:
                    if self.required:
                        raise RequiredException
                    else:
                        raise exception
                value = self.default
            if self.invalid:
                raise InvalidException

            results = rule_done.send(sender=self.__class__, rule=self,
                path=path, value=value)
            for receiver, response in results:
                value = response

        except TrustedException, exception:
            rule_exception.send(sender=self.__class__, rule=self,
                path=path, value=value, exception=exception)
            raise exception
        return value


    def core(self, value, path):
        u"""
        This function is called while validation.
        Subclasses can overwrite this one to define another validation mechanism.
        
        ``value`` is prepared value (striped if specified) for validation.
        
        ``path`` is the list from rules that called this validation.
        First element of this list will be first rule.
        
        Return correct value or raise TrustedException (or subclasses).
        """
        return value

class String(Rule):
    u"""
    Rule suppose that any string value is correct.
    Validation will return source value. 
    """

    pass

class Content(Rule):         
    u"""
    Rule suppose that any not empty string value is correct.
    Validation will return source value. 
    """

    def __init__(self, allow_empty=False, **kwargs):
        u"""
        Just replace default settings.
        """
        super(Content, self).__init__(allow_empty=allow_empty, **kwargs)

class Char(Content):
    u"""
    Rule suppose that any not empty string value is correct.
    Validation will return only first chat from the source value. 
    """

    def core(self, value, path):
        u"""Do it."""
        return value[:1]

class List(Rule):
    u"""
    Rule suppose that value is correct if it is in ``values``.
    Validation will return corresponding item from ``values``.
    """    

    def __init__(self, values, case_sensitive=False, return_defined=True, **kwargs):
        u"""
        ``values`` is list of allowed values. 
        
        ``case_sensitive`` if True than validation will be case sensitive.
        
        ``return_defined`` if True than return value as it was defined in ``values``.
        """
        super(List, self).__init__(**kwargs)
        self.source_values = values
        self.case_sensitive = case_sensitive
        self.return_defined = return_defined

        self.values = []
        for value in self.values:
            value = unicode(value)
            if not self.case_sensitive:
                value = value.lower()
            self.values.append(value)


    def core(self, value, path):
        u"""Do it."""
        if not self.case_sensitive:
            value = value.lower()
        if value not in self.values:
            raise IncorrectException
        if not self.case_sensitive and self.return_defined:
            value = self.source_values[self.values.index(value)]
        return value
        

class Url(Content):
    u"""
    Rule suppose that value is correct if it is a URL with allowed ``SCHEMES``.
    Validation will return correct URL.
    """

    SCHEMES = ['http', 'https', 'shttp', 'ftp', 'sftp', 'file', 'mailto',  
        'svn', 'svn+ssh', 'telnet', 'mms', 'ed2k', 
    ]
    GLOBAL_PREFIX = 'http://'
    LOCAL_PREFIX = '/'
    ANCHOR = re.compile(r'^#\w+$')
    ANCHOR_SPACES = re.compile(r'\s')

    def __init__(self, allow_foreign=False, allow_local=True, allow_anchor=False, **kwargs):
        u"""
        ``allow_foreign`` if True then URL to foreign sites will be allowed.
        Valid example: 'http://example.com/media/img.jpg'
        
        If ``allow_foreign`` is True and ``value`` is without schema 
        and ``value`` not started with ``LOCAL_PREFIX`` ('/') then
        ``GLOBAL_PREFIX`` ('http://') will be added to the ``value``.
        
        ``allow_local`` if True then local URL will be allowed.
        Valid examples: '/media/img.jpg' , '../img.jpg'
        
        If ``allow_local`` is False and ``value`` is without schema then
        ``Site.objects.get_current()`` will be added to the ``value``.
        
        ``allow_anchor`` if True then anchor will be allowed.
        Valid example: '#start-anchor'
        """
        super(Url, self).__init__(**kwargs)
        self.allow_foreign = allow_foreign
        self.allow_local = allow_local
        self.allow_anchor = allow_anchor
        if ':' not in self.GLOBAL_PREFIX:
            self.GLOBAL_PREFIX = self.GLOBAL_PREFIX + ':'


    def core(self, value, path):
        u"""Do it."""
        value = iri_to_uri(value)
        if ':' not in value:
            if self.allow_anchor:
                spaceless = self.ANCHOR_SPACES.sub('', value)
                if self.ANCHOR.match(spaceless):
                    return spaceless
            if value.startswith(self.LOCAL_PREFIX):
                if self.allow_local:
                    return value
                else:
                    value = unicode(Site.objects.get_current()) + value
            else:
                if not self.allow_foreign:
                    return self.LOCAL_PREFIX + value
            value = self.GLOBAL_PREFIX + value
        scheme = value[:value.find(':')].lower()
        if scheme not in self.SCHEMES:
            raise IncorrectException
        return value

class RegExp(String):
    u"""
    Rule suppose that value is correct if it match specified ``regexp``.
    Validation will return first matched group.
    
    If You want to return not empty value than
    specify at least one group in ``regexp``.
    If You don`t want cut end of ``value`` than
    specify '$' char at the end of ``regexp``.
    Example:
        regexp: '[+-]?(\d*)'
        value: '+12asd'
        result of validation: '12'
        description: will pass validation and return only first group
        (only digits, without sign) and skip all following chars.
    """

    def __init__(self, regexp, case_sensitive=False, flags=0, **kwargs):
        u"""
        ``regexp`` specified regular expression to validate ``value``.
        
        ``case_sensitive`` if True than validation will be case sensitive.
        
        ``flags`` specified flags for regular expression.
        """
        super(RegExp, self).__init__(**kwargs)
        self.regexp = regexp
        self.flags = flags
        if not self.case_sensitive:
            self.flags = self.flags | re.IGNORECASE
        self.compiled = re.compile(unicode(self.regexp), self.flags)
        
    def core(self, value, path):
        """Do it."""
        match = self.compiled.match(value)
        if match is None:
            raise IncorrectException
        try:
            value = match.group(1)
        except IndexError:
            value = ''
        return value


class Or(Rule):
    u"""
    Rule suppose that value is correct if there is correct rule in ``rules`` list.
    Validation will return first correct value returned by specified ``rules``.
    If validation for all ``rules`` will fail than raise last exception.
    """
    
    def __init__(self, rules, **kwargs):
        u"""
        ``rules`` is list of rules to validate specified ``value``.
        """
        self.rules = rules
    
    def core(self, value, path):
        """Do it."""
        path = path[:] + [self]
        result = IncorrectException
        for rule in rules:
            try:
                return rule.validate(value, path)
            except TrustedException, exception:
                result = exception
        raise result


class Sequence(Content):
    SPACES = re.compile(r'\s+')
    
    def __init__(self, validator=None, delimiter_char=' ', joiner_char=None, appender_char='', **kwargs):
        super(Sequence, self).__init__(**kwargs)
        self.validator = validator
        if self.validator is None:
            self.validator = Content()
        self.delimiter_char = delimiter_char
        self.joiner_char = joiner_char
        if self.joiner_char is None:
            self.joiner_char = self.delimiter_char
        self.appender_char = appender_char

    def sequence(self, value, parts):
        result = []
        for part in parts:
            try:
                result.append(self.validator.validate(self.name, self.attr, part, 
                    path=self, data=self.data, quite=self.quite))
            except RequiredException:
                raise SequenceException
            except EmptyException:
                pass
        return result

    def core(self, value):
        if self.SPACES:
            value = self.SPACES.sub(' ', value).strip()
        parts = value.split(self.delimiter_char)
        try:
            parts = self.sequence(value, parts)
        except SequenceException:
            raise IncorrectException(value, path)
        value = self.joiner_char.join(parts)
        if parts:
            value += self.appender_char
        return unicode(value)


class Style(Sequence, Run):
    def __init__(self, trusted_list, delimiter_char=';', joiner_char='; ', appender_char=';', data=None, equivalents={}, **kwargs):
        kwargs['delimiter_char'] = delimiter_char
        kwargs['joiner_char'] = joiner_char
        kwargs['appender_char'] = appender_char
        Sequence.__init__(self, **kwargs)
        Run.__init__(self, trusted_list, equivalents)
        
    def sequence(self, value, parts):
        attrs = []
        for part in parts:
            if ':' not in part:
                continue
            part_name = part[:part.find(':')].strip()
            part_value = part[part.find(':')+1:].strip()
            attrs.append((part_name, part_value))
        tag = Tag(self.name, attrs)
        result = self.check(tag)
        if result is None:
            raise InvalidException(value, path)
        if not result:
            raise SequenceException
        return ['%s: %s' % (part_name, part_value) for part_name, part_value in tag.attrs]


class Indent(Sequence):
    # EmptyException is the same to RequiredException.
    # You may use DefaultException to skip value.
    def __init__(self, validator=None, **kwargs):
        if validator is None:
            validator = Size()
        kwargs['validator'] = validator
        super(Indent, self).__init__(**kwargs)
        
    def sequence(self, value, parts):
        if len(parts) not in [1, 2, 4]:
            return False
        result = []
        for part in parts:
            try:
                result.append(self.validator.validate(self.name, self.attr, part, 
                    path=self, data=self.data, quite=self.quite))
            except (RequiredException, EmptyException):
                raise SequenceException
        return result


class Complex(Indent):
    # EmptyException is the same to RequiredException.
    # You may use DefaultException to skip value.
    def __init__(self, trusted_sequence, **kwargs):
        super(Complex, self).__init__(**kwargs)
        self.trusted_sequence = trusted_sequence
        
    def sequence(self, value, parts):
        return self.complex(parts, 0, self.trusted_sequence, 0)    

    def complex(self, parts, part_index, list, list_index):
        if part_index >= len(parts):
            return parts
        if list_index >= len(list):
            raise SequenceException
        try:
            value = list[list_index].validate(self.name, self.attr, parts[part_index], 
                path=self, data=self.data, quite=True)
            result = self.complex(parts, part_index + 1, list, list_index + 1)
            result[part_index] = value
            return result
        except (RequiredException, EmptyException, SequenceException):
            return self.complex(parts, part_index, list, list_index + 1)


class Html(Run):
    # All constants must be lowered. 
    special_chars = [
        ('&', '&amp;'), # Must be first element in list
        ('"', '&quot;'),
        ("'", '&apos;'),
        ('<', '&lt;'),
        ('>', '&gt;'),
        #(nbsp_char, nbsp_text),
    ]
    plain_chars = [special_chars[index] for index in range(len(special_chars)-1, -1, -1)] 
    code_re = re.compile('&#(([0-9]+);?|x([0-9A-Fa-f]+);?)')
    code_re_special = dict([(0, '')] + 
        [(ord(char), string) for char, string in special_chars])  
    system_re = re.compile('[\x01-\x1F\s]+')
    
    nbsp_char = u'\xa0'
    nbsp_text = '&nbsp;'
    nbsp_re = re.compile('[' + nbsp_char + ' ]{2,}')
    
    replace_rules = { # Use unicode text for replace
    # dictionary = {tag_name: [list of rules], ...}
    # rules = ([list of attrs], new_tag_name, [list of new_attrs])
    # attrs & new_attrs = (attr, value)
#        'span':
#            [([('style', 'text-decoration: underline;'), ], u'u', []), ],
    }
    
    empty_tags = ['td', 'th', 'caption', 'a', ]
    nbsp_tag = ['td', 'th', ]
    
    start_tags = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', # normal
        'div', 'address', 'fieldset', 'ins', 'del', # w3c 
        'ul', 'ol', 'blockquote', 'table', 'pre', # TinyMCE
    ]
    default_start_tag = 'p'
    
    markupMassage = copy.copy(BeautifulSoup.MARKUP_MASSAGE)
    markupMassage.extend([(re.compile('<!-([^-])'), 
        lambda match: '<!--' + match.group(1))])

    def code_re_suber(self, match):
        try:
            if match.group(2):
                code = int(match.group(2))
            elif match.group(3):
                code = int(match.group(3), 16)
            else:
                code = 0
            if code in self.code_re_special:
                return self.code_re_special[code]
            return unichr(code)
        except (ValueError, OverflowError):
            return ''
    
    def remove_spaces(self, html):
        return self.nbsp_re.sub(self.nbsp_char, html)
    
    def prepare(self, html):
        html = html.replace('\0', '')
        new_html = self.code_re.sub(self.code_re_suber, html)
        if new_html != html:
            print '\n~pre', repr(html), '\n=pre', repr(new_html)
            html = new_html
        html = self.system_re.sub(' ', html)
        html = self.remove_spaces(html)
        return html
    
    def tag_check(self, tag):
        if tag.name not in self.trusted_dictionary:
            print '\n!not', repr(tag.name)  
            return False
        self.trusted_list = self.trusted_dictionary[tag.name]
        return self.check(tag)
        
    def tag_replace(self, tag):
        if tag.name not in self.replace_rules:
            return
        for old_attrs, new_name, new_attrs in self.replace_rules[tag.name]:
            for old_attr, old_value in old_attrs:
                if (old_attr, old_value) not in tag.attrs:
                    break
            else:
                print '\n~rep', repr(tag.name), repr(tag.attrs)
                other_attrs = [(attr, value) for attr, value in tag.attrs 
                    if (attr, value) not in old_attrs]
                other_attrs.extend(new_attrs)
                tag.name = new_name
                tag.attrs = other_attrs
                print '\n=rep', repr(tag.name), repr(tag.attrs)
                break
    
    def clear(self, soup):
        index = 0
        while index < len(soup.contents):
            if isinstance(soup.contents[index], Tag):
                self.tag_replace(soup.contents[index])
                if self.tag_check(soup.contents[index]):
                    self.clear(soup.contents[index])
                else:
                    soup.contents[index].extract()
                    continue
            elif soup.contents[index].__class__ is not NavigableString:
                soup.contents[index].extract()
                continue
            else:
                value = soup.contents[index].string
                value = self.remove_spaces(value)
                for char, string in self.special_chars:
                    value = value.replace(char, string)
                if value != soup.contents[index].string:
                    soup.contents[index].replaceWith(value)
            index = index + 1
        return soup

    def join(self, soup):
        changed = False
        index = 0
        while index < len(soup.contents) - 1:
            if (not isinstance(soup.contents[index + 1], Tag)
                and not isinstance(soup.contents[index], Tag)):
                text = soup.contents[index].string + soup.contents[index + 1].string
                text = self.prepare(text)
                if text != soup.contents[index].string:
                    soup.contents[index].replaceWith(text)
                soup.contents[index + 1].extract()
                changed = True
                continue
            index = index + 1
        return changed

    def collapse(self, soup):
        changed = True
        while changed:
            changed = False
            index = 0
            while index < len(soup.contents):
                if isinstance(soup.contents[index], Tag):
                    self.collapse(soup.contents[index])
                    if (not self.soup.isSelfClosingTag(soup.contents[index].name)
                        and soup.contents[index].name not in self.empty_tags):
                        text = soup.contents[index].renderContents(encoding=None)
                        # encoding=None: Fix bug in BeautifulSoup (don`t work with unicode)
                        text = self.prepare(text)
                        if not text or (text == ' ') or (text == self.nbsp_char 
                            and soup.contents[index].name not in self.nbsp_tag):
                            changed = True
                            if text:
                                soup.contents[index].replaceWith(text)
                            else:
                                soup.contents[index].extract()
                                continue
                index = index + 1
            if not changed:
                if self.join(soup):
                    changed = True
        return soup
        
    def collapse_root(self, soup):
        index = 0
        while index < len(soup.contents):
            if not isinstance(soup.contents[index], Tag):
                text = soup.contents[index].string
                text = self.prepare(text)
                if not text or (text == ' ') or (text == self.nbsp_char):
                    soup.contents[index].extract()
                    continue
            index = index + 1
        return soup

    def need_wrap(self, content, for_next):
        if isinstance(content, Tag):
            if content.name in self.start_tags:
                return False
        else:
            if not for_next and (content.string == '' 
                or content.string == ' ' or content.string == self.nbsp_char):
                return False
        return True
    
    def wrap(self, soup):
        index = 0
        while index < len(soup.contents):
            while index < len(soup.contents) and not self.need_wrap(soup.contents[index], False):
                index += 1
            if index >= len(soup.contents):
                break
            start = Tag(soup, self.default_start_tag)
            while index < len(soup.contents) and self.need_wrap(soup.contents[index], True):
                content = soup.contents[index].extract()
                start.append(content)
            soup.insert(index, start)
        return soup
        
    def get_plain_text(self, soup):
        result = u''
        for content in soup:
            if isinstance(content, Tag):
                result += self.get_plain_text(content)
            else:
                value = content.string
                for char, string in self.plain_chars:
                    value = value.replace(string, char)
                result += value
        return unicode(result)
        
    def get_soup(self, html):
        return BeautifulSoup(html, markupMassage=self.markupMassage,
            convertEntities=BeautifulSoup.ALL_ENTITIES) 
        
    def filter(self, html):
        self.soup = self.get_soup(html)
        self.soup = self.clear(self.soup)
        self.soup = self.collapse(self.soup)
        self.soup = self.collapse_root(self.soup)
        self.soup = self.wrap(self.soup)
        self.plain_text = self.get_plain_text(self.soup)
        return unicode(self.soup)
        
    def __init__(self, raw_html, trusted_dictionary, data=None):
    # Generate: self.html, self.plain_text
        self.trusted_dictionary = trusted_dictionary
        super(Html, self).__init__(trusted_list=[], data=data)
        BeautifulSoup.QUOTE_TAGS = {}
        self.raw_html = unicode(raw_html)
        self.html = self.raw_html
        # print '\n~run', repr(self.html)
        for iteration in xrange(TRUSTED_ITERATIONS + 1):
            for preparing in xrange(TRUSTED_PREPARINGS + 1):
                source_html = self.html
                self.html = self.prepare(self.html)
                if source_html == self.html:
                    break
            else:
                raise ValidationError('Preparing misgiving')
            source_html = self.html
            self.html = self.filter(self.html)
            if source_html == self.html:
                break
            print '\n~fil', repr(source_html)
            print '\n=fil', repr(self.html)
        else:
            raise ValidationError('Iteration misgiving')
        # print '\n=don', repr(self.html)
        
    def __str__(self):
        return self.html

    def __unicode__(self):
        return self.html
