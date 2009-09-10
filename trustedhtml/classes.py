# -*- coding: utf-8 -*-

import re
import copy
from beautifulsoup import BeautifulSoup, NavigableString, Tag
from django.utils.encoding import iri_to_uri
from django.dispatch import Signal

from signals import rule_done, rule_exception
from utils import get_cdata, get_uri, get_style

BeautifulSoup.QUOTE_TAGS = {}

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
    
class Rule(object):
    """
    Base rule class.
    All rules inherit it and overwrite ``core`` or ``__init__`` functions.
    """

    def __init__(self, required=False, default=None, allow_empty=True,
        invalid=False, data=None):
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
        
        This function will call ``prepare`` and ``core()`` functions.
        They can be overwritten by subclasses.
        """
        source = value
        try:
            try:
                if not self.allow_empty and not value:
                    raise EmptyException(self, value)
                value = self.prepare(value, path)
                value = self.core(value, path)
                if not self.allow_empty and not value:
                    raise EmptyException(self, value)
            except TrustedException, exception:
                if self.default is None:
                    if self.required:
                        raise RequiredException(*exception.args)
                    else:
                        raise exception
                value = self.default
            if self.invalid:
                raise InvalidException(self, value)

            results = rule_done.send(sender=self.__class__, rule=self,
                path=path, value=value, source=source)
            for receiver, response in results:
                value = response

        except TrustedException, exception:
            rule_exception.send(sender=self.__class__, rule=self,
                path=path, value=value, source=source, exception=exception)
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


    def prepare(self, value, path):
        """
        This function is called while validation before ``core``.
        Subclasses can overwrite this one to define another prepare mechanism.

        ``value`` is value for validation.

        ``path`` is the list of rules that called this validation.
        First element of this list will be first rule.

        Return value, prepared for ``core`` function.
        """
        return value


class String(Rule):
    """
    Rule suppose that any string value is correct.
    Validation will return striped string value if specified.
    """
    
    def __init__(self, case_sensitive=False, strip=True, **kwargs):
        """
        ``strip`` if True than remove leading and trailing whitespace.

        ``case_sensitive`` if True than validation will be case sensitive.
        
        This class don`t prepare ``value`` according to ``case_sensitive``.
        Just specified functions to do it.
        """
        super(String, self).__init__(**kwargs)
        self.case_sensitive = case_sensitive
        self.strip = strip

    
    def lower_string(self, value):
        """
        ``value`` is an object with __unicode__ method.
        ``value`` can be None.
        
        Returns ``value`` in low case if ``case_sensitive`` is True.
        """
        if value is None:
            return value
        if self.case_sensitive:
            return unicode(value)
        else:
            return unicode(value).lower()


    def lower_list(self, values):
        """
        ``values`` is list of objects.
        ``value`` can be None.
        
        Returns list of ``values`` in low case if ``case_sensitive`` is True.
        """
        if values is None:
            return values
        return [self.lower_string(value)
            for value in values]


    def prepare(self, value, path):
        """Do it."""
        value = super(String, self).prepare(value, path)
        if value is None:
            value = ''
        value = unicode(value)
        if self.strip:
            value = value.strip()
        return value


class List(String):
    """
    Rule suppose that value is correct if it is in ``values``.
    Validation will return corresponding item from ``values``.
    """    

    def __init__(self, values, return_defined=True, **kwargs):
        """
        ``values`` is list of allowed values. 
        
        ``return_defined`` if True than return value as it was defined in ``values``.
        """
        super(List, self).__init__(**kwargs)
        self.source_values = values
        self.return_defined = return_defined
        self.values = self.lower_list(self.source_values)


    def core(self, value, path):
        """Do it."""
        value = super(List, self).core(value, path)
        source = value
        value = self.lower_string(value)
        if value not in self.values:
            raise IncorrectException(self, value)
        if not self.case_sensitive:
            if self.return_defined:
                value = self.source_values[self.values.index(value)]
            else:
                value = source
        return value


class RegExp(String):
    """
    Rule suppose that value is correct if it match specified ``regexp``.
    Validation will return expanded match object.
    """

    def __init__(self, regexp, flags=0, expand=r'\1', **kwargs):
        """
        ``regexp`` specified string with regular expression to validate ``value``.
        Specify '$' char at the end of expression to avoid cutting end of string. 
        
        ``flags`` specified flags for regular expression.
        
        ``expand`` is string using to expand match objects
        and to return result of validation.

        Example of validation:
            regexp: r'([-+]?\d*),(?P<a>\d*)$'
            expand: r'\g<a>;\1'
            value: '-12,34'
            result: '34;-12'
            description: return group "a" and first group.
            '$' at the and of string will prevent skipping all following chars.
        """
        super(RegExp, self).__init__(**kwargs)
        self.regexp = regexp
        self.flags = flags
        self.expand = expand
        if not self.case_sensitive:
            self.flags = self.flags | re.IGNORECASE
        self.compiled = re.compile(unicode(self.regexp), self.flags)

    def core(self, value, path):
        """Do it."""
        value = super(RegExp, self).core(value, path)
        match = self.compiled.match(value)
        if match is None:
            raise IncorrectException(self, value)
        value = match.expand(self.expand)
        return value


class Uri(RegExp):
    """
    Rule suppose that value is correct if it is allowed URI.
    Validation will return correct URI.
    """
    
    def __init__(self, allow_sites=None, allow_schemes=[
            'http', 'https', 'shttp', 'ftp', 'sftp', 'file', 'mailto',  
            'svn', 'svn+ssh', 'telnet', 'mms', 'ed2k', 
        ], local_sites=[], local_schemes=['http', ], is_image=False, **kwargs):
        """
        ``allow_sites`` is list of allowed sites or is None to allow all sites.

        To allow only your sites, you can use:
        [site.domain for site in django.contrib.sites.models.Site.objects.all()]
        
        To disallow all sites (only paths will be available), you can use:
        []
        
        ``allow_schemes`` is list of allowed schemes for URIs.
        
        ``local_sites`` is list of sites for witch
        scheme and site-name will be removed from uri.
        
        ``local_schemes`` is list of schemes that can be removed.
        Only uris with such scheme will be cut.
        
        ``is_image`` indicate that this url must be as image.
        This class not support such validation,
        but this attribute can be used by signals.
        """
        super(Uri, self).__init__(
            regexp=r'^(([^:/?#]+):)?(//([^/?#]*))?([^?#]*)(\?([^#]*))?(#(.*))?',
            case_sensitive=False, **kwargs)
        self.allow_sites = self.lower_list(allow_sites)
        self.allow_schemes = self.lower_list(allow_schemes)
        self.local_sites = self.lower_list(local_sites)
        if self.local_sites is None:
            self.local_sites = []
        self.local_schemes = self.lower_list(local_schemes)
        self.is_image = is_image

    def prepare(self, value, path):
        """
        Correct escaped-chars (%hh).
        We don`t replace escaped-chars, just replace "%Z" with "%25Z".
        Escaped-chars not allowed in scheme and authority paths,
        so we can trust prepared values.
        """
        value = super(Uri, self).prepare(value, path)
        value = get_uri(value)
        return value

    def split(self, uri):
        """
        Return tuple (scheme, authority, path, query, fragment) for given ``uri``.
        """
        match = self.compiled.match(uri)
        return (match.group(2), match.group(4), match.group(5), match.group(7), match.group(9))

    
    def build(self, scheme, authority, path, query, fragment):
        """
        Return uri from given (scheme, authority, path, query, fragment).
        """
        result = ''
        if scheme is not None:
            result += scheme + ':'
        if authority is not None:
            result += '//' + authority
        if path is not None:
            result += path
        if query is not None:
            result += '?' + query
        if fragment is not None:
            result += '#' + fragment
        return result

    def core(self, value, path):
        """Do it."""
        value = String.core(self, value, path)
        scheme_source, authority_source, path, query, fragment = self.split(value)
        scheme = self.lower_string(scheme_source)
        authority = self.lower_string(authority_source)
        if scheme is not None:
            if scheme not in self.allow_schemes:
                raise IncorrectException(self, value)
        if authority is not None and self.allow_sites is not None:
            if authority not in self.allow_sites:
                raise IncorrectException(self, value)
        if (scheme is None or scheme in self.local_schemes)\
            and (authority in self.local_sites):
            scheme = None
            authority = None
            if not path and not query and not fragment:
                path = '/'
        value = self.build(scheme, authority, path, query, fragment)
        return value


class No(Rule):
    """
    Rule suppose that value never is correct.
    Validation always will raise IncorrectException.
    """
    
    def core(self, value, path):
        """Do it."""
        raise IncorrectException


class And(Rule):
    """
    Rule suppose that value is correct if it corresponding to all ``rules``.
    Validation will return correct value from the last rule.
    First rule will validate specified ``value``,
    second rule will validate result of first validation, etc.
    """
    
    def __init__(self, rules, **kwargs):
        """
        ``rules`` is list of rules to validate specified ``value``.
        """
        super(And, self).__init__(**kwargs)
        self.rules = rules
    
    def core(self, value, path):
        """Do it."""
        value = super(And, self).core(value, path)
        path = path[:] + [self]
        for rule in self.rules:
            value = rule.validate(value, path)
        return value


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
        super(Or, self).__init__(**kwargs)
        self.rules = rules
    
    def core(self, value, path):
        """Do it."""
        value = super(Or, self).core(value, path)
        path = path[:] + [self]
        last = IncorrectException
        for rule in self.rules:
            try:
                return rule.validate(value, path)
            except InvalidException, exception:
                raise exception
            except TrustedException, exception:
                last = exception
        raise last


class Sequence(String):
    """
    Rule suppose that value is correct if each part of value,
    divided by ``regexp`` matches specified ``rule``.
    Validation will return joined parts of value.
    """
    
    def __init__(self, rule, regexp=r'\s+', flags=0, min_split=0, max_split=0, 
        join_string=' ', prepend_string='', append_string='', **kwargs):
        """
        ``rule`` is the rule that will be called to validate each path of value.
        
        ``regexp`` specified string with regular expression
        to split specified value.
        
        ``flags`` specified flags for regular expression.
        
        ``min_split`` specified minimum allowed number of parts.
        Validation will raise IncorrectException if number of parts is less.
        
        ``max_split`` specified maximum allowed number of parts.
        Validation will raise IncorrectException if number of parts is less.
        
        ``join_string`` is string that will be used to join back
        validated parts of value.
        
        ``prepend_string`` is string that will be inserted before joined value.
        
        ``append_string`` is string that will be added to the end of joined value.
        """
        super(Sequence, self).__init__(**kwargs)
        self.rule = rule
        self.regexp = regexp
        self.flags = flags
        if not self.case_sensitive:
            self.flags = self.flags | re.IGNORECASE
        self.compiled = re.compile(unicode(self.regexp), self.flags)
        self.min_split = min_split
        self.max_split = max_split
        self.join_string = join_string
        self.prepend_string = prepend_string
        self.append_string = append_string

    def sequence(self, values, path):
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
            result.append(self.rule.validate(value, path))
        return result

    def core(self, value, path):
        """Do it."""
        value = super(Sequence, self).core(value, path)
        values = self.compiled.split(value)
        if (len(values) < self.min_split) or (self.max_split and len(values) > self.max_split):
            raise IncorrectException(self, value)
        path = path[:] + [self]
        values = self.sequence(values, path)
        value = self.prepend_string + self.join_string.join(values) + self.append_string
        return value


class Complex(Sequence):
    """
    Rule suppose that value is correct if each part of value,
    divided by ``regexp`` matches one of specified
    ``rules`` list in corresponding order.
    Validation will return joined parts of value.
    """

    def __init__(self, rules, **kwargs):
        """
        ``rules`` is list of rules for validation.
        """
        super(Complex, self).__init__(rule=None, **kwargs)
        self.rules = rules

    def sequence(self, values, path):
        """Do it."""
        return self.complex(values, path, 0, 0)    

    def complex(self, values, path, value_index, rule_index):
        """
        This function is called by ``sequence`` function.
         
        ``values`` is list of parts of specified ``value``.

        ``path`` is the list of rules that called this validation + self object.
        
        ``value_index`` is index in ``values`` list to be processed.

        ``rule_index`` is index in ``rules`` list to be processed.
        
        Return correct list of parts of value or raise IncorrectException or InvalidException.
        """
        if value_index >= len(values):
            return values
        if rule_index >= len(self.rules):
            raise IncorrectException(self, values)
        try:
            value = self.rules[rule_index].validate(values[value_index], path)
            result = self.complex(values, path, value_index + 1, rule_index + 1)
            result[value_index] = value
            return result
        except InvalidException, exception:
            raise exception
        except TrustedException:
            return self.complex(values, path, value_index, rule_index + 1)


class Validator(object):
    """
    Provide mechanism to validate list of values (tag attributes or style properties)
    by corresponding rules.
    """

    def __init__(self, rules,  **kwargs):
        """
        ``rules`` is dictionary in witch key is name of property
        (or tag attribute) and value is corresponding rule.
        """
        self.rules = rules

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
        for name, rule in self.rules.iteritems():
            try:
                try:
                    value = values[name]
                except IndexError:
                    raise EmptyException(self, None)
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


class Style(Sequence, Validator):
    """
    Rule suppose that value is correct if each part of ``value``,
    is pair (property_name, property_value) and each property_name
    has valid property_value corresponding to ``rules`` dictionary.
    Validation will return joined only valid pairs.
    """

    def __init__(self, rules, **kwargs):
        """
        ``rules`` is dictionary in witch key is name of property
        (or tag attribute) and value is corresponding rule.
        """
        Sequence.__init__(self, rule=None, regexp=r'\s*;\s*',
            join_string='; ', append_string=';', **kwargs)
        Validator.__init__(self, rules=rules, **kwargs)
        
    def prepare(self, value, patj):
        """Do it."""
        value = super(Style, self).prepare(value, path)
        value = get_style(value)
        return value

    def sequence(self, values, path):
        """Do it."""
        properties = []
        for value in values:
            if ':' not in value:
                continue
            property_name = value[:value.find(':')].strip()
            property_value = value[value.find(':')+1:].strip()
            properties.append((property_name, property_value))
        try:
            properties = self.check(properties, path)
        except RequiredException, exception:
            raise IncorrectException(*exception.args)
        return ['%s: %s' % (property_name, property_value)
            for property_name, property_value in properties]


class Element(Rule, Validator):
    """
    Rule suppose that value is correct if ``value`` is LIST OF PAIRS
    (attribute_name, attribute_value) and each attribute_name
    has valid attribute_value corresponding to ``rules`` dictionary.
    Validation will return list of valid pairs (attribute_name, attribute_value).
    """

    def __init__(self, rules={}, allow_empty=False,
        optional_start=False, optional_end=False, empty_tag=False, 
        root_tag=False, save_content=True, **kwargs):
        """
        ``rules`` is dictionary in witch key is name of property
        (or tag attribute) and value is corresponding rule.
        
        ``optional_start`` start of this element is optional.

        ``optional_end`` end of this element is optional.
        
        ``empty_tag`` tag must be empty.
        
        ``root_tag`` tag can be in the root of document.
        
        ``save_content`` whether content of incorrect tag must be saved
        to parent tag. 
        """
        if self.empty_tag:
            allow_empty = True
        Rule.__init__(self, allow_empty=allow_empty, **kwargs)
        Validator.__init__(self, rules=rules, **kwargs)
        self.optional_start = optional_start
        self.optional_end = optional_end
        self.empty_tag = empty_tag
        self.root_tag = root_tag
        self.save_content = save_content
        
    def prepare(self, value, path):
        """Do it."""
        value = super(Attributes, self).prepare(value, path)
        value = [(attribute_name, get_cdata(attribute_value))
            for attribute_name, attribute_value in value]
        return value
        
    def core(self, value, path):
        """Do it."""
        try:
            return self.check(value, path)
        except (RequiredException, InvalidException), exception:
            raise IncorrectException(*exception.args)


class Html(String):
    """
    Rule suppose that value is correct if it can be fixed
    over ``fix_number`` iterations.
    And chars in value can be prepared for fixing
    over ``prepare_number`` iterations per fix.
    Validation will return valid tuple (valid_html, plain_text).
    """

    # All constants must be lowered. 
    SPECIAL_CHARS = [
        ('&', '&amp;'), # Must be first element in list
        ('"', '&quot;'),
        ("'", '&apos;'),
        ('<', '&lt;'),
        ('>', '&gt;'),
        #(NBSP_CHAR, NBSP_TEXT),
    ]
    PLAIN_CHARS = [SPECIAL_CHARS[index] for index in range(len(SPECIAL_CHARS)-1, -1, -1)]
    CODE_RE = re.compile('&#(([0-9]+);?|x([0-9A-Fa-f]+);?)')
    CODE_RE_SPECIAL = dict([(0, '')] + 
        [(ord(char), string) for char, string in SPECIAL_CHARS])  
    SYSTEM_RE = re.compile('[\x01-\x1F\s]+')

    NBSP_CHAR = u'\xa0'
    NBSP_TEXT = '&nbsp;'
    NBSP_RE = re.compile('[' + NBSP_CHAR + ' ]{2,}')
    
    DEFAULT_ROOT_TAG = 'p'
    
    MARKUP_MASSAGE = BeautifulSoup.MARKUP_MASSAGE + [
        (re.compile('<!-([^-])'), lambda match: '<!--' + match.group(1))
    ]

    def __init__(self, rules, fix_number=2, prepare_number=2, **kwargs):
        """
        ``rules`` is dictionary in witch key is name of property
        (or tag attribute) and value is corresponding rule.
        
        ``fix_number`` specified number of maximum attempts to fix value.

        ``prepare_number`` specified number of maximum attempts to prepare value.
        """
        super(Html, self).__init__(**kwargs)
        self.rules = rules
        self.fix_number = fix_number
        self.prepare_number = prepare_number
        self.empty_tags = []
        self.nbsp_tags = []
        self.root_tags = []
        for name, rule in self.rules.iteritems():
            if rule.allow_empty or rule.default is not None:
                self.empty_tags.append(name)
            if rule.default is not None:
                self.nbsp_tags.append(name)
            if getattr(rule, 'root_tag', False):
                self.root_tags.append(name)
                

    def remove_spaces(self, value):
        """Removes spaces from ``value``"""
        return self.NBSP_RE.sub(self.NBSP_CHAR, value)

    def prepare(self, value):
        """Prepare chars in ``value``. Replace system values."""
        def code_re_sub(match):
            try:
                if match.group(2):
                    code = int(match.group(2))
                elif match.group(3):
                    code = int(match.group(3), 16)
                else:
                    code = 0
                if code in self.CODE_RE_SPECIAL:
                    return self.CODE_RE_SPECIAL[code]
                return unichr(code)
            except (ValueError, OverflowError):
                return ''
        value = value.replace('\0', '')
        value = self.CODE_RE.sub(code_re_sub, value)
        value = self.SYSTEM_RE.sub(' ', value)
        value = self.remove_spaces(value)
        return value


    def clear(self, soup, path):
        index = 0
        while index < len(soup.contents):
            if isinstance(soup.contents[index], Tag):
                rule = self.rules.get(soup.contents[index].name, None)
                try:
                    if rule is None:
                        raise IncorrectException(self, None)
                    rule.validate(soup.contents[index].attrs, path)
                except TrustedException:
                    element = soup.contents[index].extract()
                    if rule is not None and getattr(rule, 'save_content', False):
                        for content in element.contents:
                            soup.insert(index, content)
                    continue
                self.clear(soup.contents[index])
            elif soup.contents[index].__class__ is NavigableString:
                value = soup.contents[index].string
                value = self.remove_spaces(value)
                for char, string in self.SPECIAL_CHARS:
                    value = value.replace(char, string)
                if value != soup.contents[index].string:
                    soup.contents[index].replaceWith(value)
            else:
                soup.contents[index].extract()
                continue
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
                        if not text or (text == ' ') or (text == self.NBSP_CHAR 
                            and soup.contents[index].name not in self.nbsp_tags):
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
                if not text or (text == ' ') or (text == self.NBSP_CHAR):
                    soup.contents[index].extract()
                    continue
            index = index + 1
        return soup

    def need_wrap(self, content, for_next):
        if isinstance(content, Tag):
            if content.name in self.root_tags:
                return False
        else:
            if not for_next and (content.string == '' 
                or content.string == ' ' or content.string == self.NBSP_CHAR):
                return False
        return True
    
    def wrap(self, soup):
        index = 0
        while index < len(soup.contents):
            while index < len(soup.contents) and not self.need_wrap(soup.contents[index], False):
                index += 1
            if index >= len(soup.contents):
                break
            start = Tag(soup, self.DEFAULT_ROOT_TAG)
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
                for char, string in self.PLAIN_CHARS:
                    value = value.replace(string, char)
                result += value
        return result

    def fix(self, value, path):
        source = value
        soup = BeautifulSoup(value, markupMassage=self.MARKUP_MASSAGE,
            convertEntities=BeautifulSoup.ALL_ENTITIES)
        soup = self.clear(soup, path)
        soup = self.collapse(soup)
        soup = self.collapse_root(soup)
        soup = self.wrap(soup)
        plain = self.get_plain_text(soup)
        return (unicode(soup), unicode(plain))

    def core(self, value, path):
        """Do it."""
        path = path[:] + [self]
        value = String.core(self, value, path)
        for iteration in xrange(self.fix_number + 1):
            for preparing in xrange(self.prepare_number + 1):
                source = value
                value = self.prepare(value)
                if source == value:
                    break
            else:
                raise InvalidException(self, 'Too much attempts to prepare value')
            source = value
            value, plain = self.fix(value, path)
            if source == value:
                break
        else:
            raise InvalidException(self, 'Too much attempts to fix value')
        return (value, plain)
