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
    """
    Base trustedhtml exception.
    """
    pass

class EmptyException(TrustedException):
    """
    Raised when value is empty and ``allow_empty`` flag is False.
    
    This exception means that attribute must be removed. 
    """
    pass
 
class IncorrectException(TrustedException):
    """
    Raised when value is incorrect. 
    
    This exception means that attribute must be removed. 
    """
    pass
 
class RequiredException(TrustedException):
    """
    Raised when value is empty and ``required`` flag is True.
    
    This exception means that hole item must be removed.
    """
    pass
 
class InvalidException(TrustedException):
    """
    Raised when value pass check and invalid flag is True.
    
    This exception means that hole TAG must be removed.
    """
    pass
    
class SequenceException(TrustedException):
    """
    Raised when element not corresponded to sequence. 
    
    Example: color is not specified for "border" style property
    """
    pass


class Rule(object):
    """
    Base rule class.
    All rules inherit it and overwrite ``core`` or ``__init__`` functions.
    """

    def __init__(self, required=False, default=None, allow_empty=True,
        invalid=False, data=None, **kwargs):
        """
        Sets behaviour for the rule:

        ``required`` if True than value is required.
        Example: attribute "src" for tag "img".

        ``default`` if is not None and validation fail than will return this one.
        Example: attribute "alt" for tag "img". 

        ``allow_empty`` if True than value can be empty.
        Example: attribute "width" for tag "img".

        ``invalid`` if True than result of validation will be inverted.
        Also this mean that hole TAG must be removed if such rule succeed.
        Example: "none" value for "display" style property
        (we want to remove such tag).

        ``data`` any extended data, usually used by signals.
        """
        self.required = required
        if default is not None:
            default = unicode(default)
        self.default = default
        self.allow_empty = allow_empty
        self.invalid = invalid
        self.data = data


    def validate(self, value, path=[]):
        """
        Main interface function. Call it to validate specified ``value``.
        
        Returns correct value or raise exception.
        
        ``path`` is the list of rules that called this validation.
        First element of this list will be first rule.
        
        This function will call ``core()`` that can be overwritten by subclasses.
        """
        try:
            try:
                if not self.allow_empty and not value:
                    raise EmptyException
                value = self.core(value, path)
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
        """
        This function is called while validation.
        Subclasses can overwrite this one to define another validation mechanism.

        ``value`` is value for validation.

        ``path`` is the list of rules that called this validation.
        First element of this list will be first rule.

        Return correct value or raise TrustedException (or subclasses).
        """
        return value


class Validator(object):
    """
    Provide mechanism to validate list of values (tag attributes or style properties)
    by corresponding rules.
    """

    def __init__(self, rules, equivalents={}, **kwargs):
        """
        ``rules`` is dictionary in witch key is name of property
        (or tag attribute) and value is corresponding rule.
        
        ``equivalents`` is dictionary in witch key is name of property
        specified in ``rules`` and value is list of properties` names
        (or tag attribute) that must be validated by the same rule.  
        """
        self.rules = rules
        self.equivalents = equivalents

    def check(self, values, path):
        """
        Check list of ``values`` (tag attributes or style properties)
        corresponding to specified rules.

        ``values`` list of (property, value) pairs, as 2-tuples.
        
        ``path`` is the list of rules that called this validation.
        First element of this list will be first rule.
        
        Return list of correct values depending on rules.
        Or raise exceptions:

        ``RequiredException`` means that list of values not corresponding
        to rules and instance that contains it must be removed.

        ``InvalidException`` means that list of values not corresponding
        to rules and TAG that contains it must be removed.
        """
        if not self.rules:
            return []
        correct = {}
        values = dict(values)
        for base_name, rule in self.rules.iteritems():
            names = [base_name] + self.equivalents.get(base_name, [])
            for name in names:
                try:
                    try:
                        value = values[name]
                    except IndexError:
                        raise EmptyException
                    correct[name] = rule.validate(value, path)
                except (EmptyException, IncorrectException):
                    pass
        # Order values is source ordering. New values will be appended.
        order = [attr for attr, value in values]
        append = [attr for attr, value in correct.iteritems() if attr not in order]
        order.extend(append)
        values = [(order.index(attr), attr, value) for attr, value in correct.iteritems()]
        values.sort()
        return [(item, value) for index, item, value in values]


class Or(Rule):
    """
    Rule suppose that value is correct if there is correct rule in ``rules`` list.
    Validation will return first correct value returned by specified ``rules``.
    If validation for all ``rules`` will fail than raise last exception.
    If rule raise InvalidException it will be immediately raised.
    """
    
    def __init__(self, rules, **kwargs):
        """
        ``rules`` is list of rules to validate specified ``value``.
        """
        self.rules = rules
    
    def core(self, value, path):
        """Do it."""
        value = super(Or, self).core(value, path)
        path = path[:] + [self]
        last = IncorrectException
        for rule in rules:
            try:
                return rule.validate(value, path)
            except InvalidException:
                raise InvalidException
            except TrustedException, exception:
                last = exception
        raise last


class String(Rule):
    """
    Rule suppose that any string value is correct.
    Validation will return striped string value if specified. 
    """
    
    def __init__(self, strip=True, kwargs):
        """
        ``strip`` if True than remove leading and trailing whitespace.
        """
        self.strip = strip
        super(Content, self).__init__(**kwargs)
    
    def core(self, value, path):
        """Do it."""
        value = super(String, self).core(value, path)
        if value is None:
            value = ''
        value = unicode(value)
        if self.strip:
            value = value.strip()
        return value

class Content(String):
    """
    Rule suppose that any not empty string value is correct.
    Validation will return source value. 
    """

    def __init__(self, allow_empty=False, **kwargs):
        """
        Just replace default settings.
        """
        super(Content, self).__init__(allow_empty=allow_empty, **kwargs)

class Char(Content):
    """
    Rule suppose that any not empty string value is correct.
    Validation will return only first chat from the source value. 
    """

    def core(self, value, path):
        """Do it."""
        value = super(Char, self).core(value, path)
        return value[:1]


class List(String):
    """
    Rule suppose that value is correct if it is in ``values``.
    Validation will return corresponding item from ``values``.
    """    

    def __init__(self, values, case_sensitive=False, return_defined=True, **kwargs):
        """
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
        """Do it."""
        value = super(List, self).core(value, path)
        if not self.case_sensitive:
            value = value.lower()
        if value not in self.values:
            raise IncorrectException
        if not self.case_sensitive and self.return_defined:
            value = self.source_values[self.values.index(value)]
        return value


class Url(Content):
    """
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
        """
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
        """Do it."""
        value = super(Url, self).core(value, path)
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
    """
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

    def __init__(self, regexp, case_sensitive=False, regexp_flags=0, **kwargs):
        """
        ``regexp`` specified string with regular expression to validate ``value``.
        
        ``case_sensitive`` if True than validation will be case sensitive.
        
        ``regexp_flags`` specified flags for regular expression.
        """
        super(RegExp, self).__init__(**kwargs)
        self.regexp = regexp
        self.regexp_flags = regexp_flags
        if not self.case_sensitive:
            self.regexp_flags = self.regexp_flags | re.IGNORECASE
        self.compiled = re.compile(unicode(self.regexp), self.regexp_flags)
        
    def core(self, value, path):
        """Do it."""
        value = super(RegExp, self).core(value, path)
        match = self.compiled.match(value)
        if match is None:
            raise IncorrectException
        try:
            value = match.group(1)
        except IndexError:
            value = ''
        return value


class Sequence(String):
    """
    Rule suppose that value is correct if each path of value,
    divided by ``delimiter_regexp`` match specified ``rule``.
    Validation will return first matched group.
    """
    
    def __init__(self, rule, delimiter_regexp='\s+', case_sensitive=False, 
        regexp_flags=0, join_string=' ', append_string=None, **kwargs):
        """
        ``rule`` is the rule that will be called to validate each path of value.
        
        ``delimiter_regexp`` specified string with regular expression
        to split specified value.
        
        ``case_sensitive`` if True than validation will be case sensitive.
        
        ``regexp_flags`` specified flags for regular expression.
        
        ``join_string`` is string that will be used to join back
        validated parts of value.
        
        ``append_string`` is string that will be added to the end of joined value.
        """
        super(Sequence, self).__init__(**kwargs)
        self.delimiter = delimiter
        self.regexp_flags = regexp_flags
        if not self.case_sensitive:
            self.regexp_flags = self.regexp_flags | re.IGNORECASE
        self.compiled = re.compile(unicode(self.delimiter), self.regexp_flags)
        
        self.rule = rule
        self.join_string = join_string
        self.append_string = append_string

    def check(self, values, path):
        """
        This function is called from ``core`` function.
        Subclasses can overwrite this one to define another validation mechanism.

        ``values`` is list of parts of specified ``value``.

        ``path`` is the list of rules that called this validation + self object.
        So you can pass this value for subvalidations.
        
        Return correct list of parts of value or raise TrustedException (or subclasses).
        """
        result = []
        for value in values:
            try:
                result.append(self.rule.validate(value, path))
            except RequiredException:
                raise SequenceException
            except EmptyException:
                pass
        return result

    def core(self, value, path):
        """Do it."""
        value = super(Sequence, self).core(value, path)
        path = path[:] + [self]
        values = self.compiled.split(value)
        try:
            values = self.check(values, path)
        except SequenceException:
            raise IncorrectException
        value = self.join_string.join(values)
        if append_string:
            value += self.append_string
        return value


class Style(Sequence, Validator):
    def __init__(self, rules, equivalents={}, delimiter_regexp='\s*;\s*', join_string='; ', append_string=';', **kwargs):
        super(Style, self).__init__(delimiter_regexp=delimiter_regexp, 
            join_string=join_string, append_string=append_string, **kwargs)
        Validator.__init__(self, rules=rules, equivalents=equivalents, **kwargs)
        
    def check(self, values, path):
        properties = []
        for value in values:
            if ':' not in value:
                continue
            property_name = value[:value.find(':')].strip()
            property_value = value[value.find(':')+1:].strip()
            properties.append((property_name, partproperty_value))
        tag = Tag(self.name, )
        try:
            properties = self.check(properties)
        except InvalidException:
            raise InvalidException
        except TrustedException:
            raise SequenceException
        return ['%s: %s' % (property_name, property_value)
            for property_name, property_value in properties]


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


class Html(Validator):
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
        self.rules = self.trusted_dictionary[tag.name]
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
        super(Html, self).__init__(rules=[], data=data)
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
