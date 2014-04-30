# -*- coding: utf-8 -*-

import re
from beautifulsoup import BeautifulSoup, NavigableString, Tag, buildTagMap

from trustedhtml import settings
from trustedhtml.signals import rule_done, rule_exception
from trustedhtml.utils import get_cdata, get_style
from urlmethods import urlsplit, urljoin, urlfix, remote_check, local_check

BeautifulSoup.QUOTE_TAGS = {}
BeautifulSoup.SELF_CLOSING_TAGS = buildTagMap(None, [
    'area', 'base', 'basefont', 'br', 'col', 'frame', 'hr',
    'img', 'input', 'isindex', 'link', 'meta', 'param',
    # I don`t what is: 'spacer',
])


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


class InvalidException(TrustedException):
    """
    Raised when value pass check and invalid flag is True.
    
    This exception means that hole item must be removed.
    """
    pass


class ElementException(TrustedException):
    """
    Raised when value fail check and tag_exception flag is True.
    
    This exception means that hole TAG must be removed.
    This exception will raise throw all rules to element-rule.
    """
    pass


class Rule(object):
    """
    Base rule class.
    All rules inherit it and overwrite ``core`` or ``__init__`` functions.
    """

    def __init__(
            self, allow_empty=True, default=None, invalid=False,
            element_exception=False, data=None):
        """
        Sets behaviour for the rule:

        ``allow_empty`` if False than value can`t be empty.
        For example: attribute "width" for tag "img".

        ``default`` if it is not None and validation fail than will return this one.
        For example: attribute "alt" for tag "img". 

        ``invalid`` if True than result of validation will be inverted.
        So if validation will pass than InvalidException will be raised.
        It if validation will fail than source value will be returned as correct value.
        
        ``element_exception`` if True and validation will failed than
        hole TAG must be removed.

        ``data`` any extended data, usually used by signals.
        """
        self.allow_empty = allow_empty
        self.default = default
        self.invalid = invalid
        self.element_exception = element_exception
        self.data = data

    def validate(self, value, path=None):
        """
        Main interface function. Call it to validate specified ``value``.
        
        Returns correct value or raise exception.
        
        ``path`` is the list of rules that called this validation.
        First element of this list will be first rule.
        
        This function will call ``preprocess``, ``core`` and 
        ``postprocess`` functions.
        They can be overwritten by subclasses.
        """
        if path is None:
            path = []
        source = value
        try:
            try:
                value = self.preprocess(value, path)
                value = self.core(value, path)
                value = self.postprocess(value, path)
                if self.invalid:
                    raise InvalidException(self, value)
            except ElementException, exception:
                raise exception
            except TrustedException, exception:
                if self.element_exception:
                    raise ElementException(*exception.args)
                if self.default is not None:
                    value = self.default
                elif self.invalid and exception is not InvalidException:
                    value = source
                else:
                    raise exception

            results = rule_done.send(
                sender=self.__class__, rule=self,
                path=path, value=value, source=source)
            for receiver, response in results:
                value = response

        except TrustedException, exception:
            rule_exception.send(
                sender=self.__class__, rule=self,
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

    def preprocess(self, value, path):
        """
        This function is called while validation before ``core``.
        It checks ``value`` according to ``allow_empty`` property.  
        Subclasses can overwrite this one to define another preprocess mechanism.

        ``value`` is value for validation.

        ``path`` is the list of rules that called this validation.
        First element of this list will be first rule.

        Return prepared value for ``core`` function.
        """
        if not self.allow_empty and not value:
            raise EmptyException(self, value)
        return value

    def postprocess(self, value, path):
        """
        This function is called while validation after ``core``.
        It checks ``value`` according to ``allow_empty`` property.  
        Subclasses can overwrite this one to define another postprocess mechanism.

        ``value`` is value for validation.

        ``path`` is the list of rules that called this validation.
        First element of this list will be first rule.

        Return prepared value after ``core`` function.
        """
        if not self.allow_empty and not value:
            raise EmptyException(self, value)
        return value


class String(Rule):
    """
    Rule suppose that any string value is correct.
    Validation will return striped string value if specified.
    """

    def __init__(self, case_sensitive=False, strip=True, allow_empty=False, **kwargs):
        """
        ``strip`` if True than remove leading and trailing whitespace.

        ``case_sensitive`` if True than validation will be case sensitive.
        
        This class don`t prepare ``value`` according to ``case_sensitive``.
        Just specified functions to do it.
        """
        super(String, self).__init__(allow_empty=allow_empty, **kwargs)
        if self.default is not None:
            self.default = unicode(self.default)
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
        if values is None or values is False or values is True:
            return values
        return [
            self.lower_string(value)
            for value in values]

    def preprocess(self, value, path):
        """Do it."""
        value = super(String, self).preprocess(value, path)
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


class Uri(String):
    """
    Rule suppose that value is correct if it is allowed URI.
    Validation will return correct URI.
    """
    LINK = 0
    IMAGE = 1
    OBJECT = 2

    def __init__(
            self, type=LINK, allow_sites=None, allow_schemes=None,
            cut_sites=None, cut_schemes=None, verify_sites=None, verify_schemes=None,
            verify_local=None, local_sites=None, local_schemes=None,
            **kwargs):
        """
        ``type`` indicate that this url must be an image.
        This class not support such validation,
        but this attribute can be used by rules or signals.
        
        ``is_object`` indicate that this url must be an embedded object. 
        This class not support such validation,
        but this attribute can be used by rules or signals.

        All lists passed to this function can be:
            list of strings with allowed values.
            True to allow all values.
            False or disable all values.
            None is used not set default value (from settings.py).

        ``allow_sites`` is list with names of allowed sites.
        You can use your registered sites like this:
        [site.domain for site in django.contrib.sites.models.Site.objects.all()]
        
        ``allow_schemes`` is list of allowed schemes for URIs.
        
        ``cut_sites`` is list of sites for witch
        scheme and site`s name will be removed from url.
        Cut operations will be applied before any other validations.
        
        ``cut_schemes`` is list of schemes that can be removed.
        Only urls with such scheme will be cut.
        
        ``verify_sites`` is list of sites to be verified.
        Validation will try to fetch specified url for such sites. 
        
        ``verify_schemes`` is list of allowed schemes for verification.
        
        ``verify_local`` specify verification mechanism:
            string to specify host to fetch urls without host name.
            You can use:
            django.contrib.sites.models.Site.objects.get_current().domain

            False to disable any verification of local urls.

            True to enable verification by using django.test.Client.
            You must use it if your server is running in one thread
            (and was not forked).
            In such case requests to it self can`t be received.
            
        ``local_sites`` is list of sites to be recognized as local. 
        
        ``local_schemes`` is list of schemes for local verification.
        
        ``verify_user_agent`` is name of user agent for verification.
        
        This class ignore ``case_sensitive`` considered it is False.
        """
        super(Uri, self).__init__(case_sensitive=False, **kwargs)
        if allow_sites is None:
            if type == self.LINK:
                allow_sites = settings.TRUSTEDHTML_LINK_SITES
            elif type == self.IMAGE:
                allow_sites = settings.TRUSTEDHTML_IMAGE_SITES
            elif type == self.OBJECT:
                allow_sites = settings.TRUSTEDHTML_OBJECT_SITES
            else:
                allow_sites = False
        if allow_schemes is None:
            allow_schemes = settings.TRUSTEDHTML_ALLOW_SCHEMES
        if cut_sites is None:
            cut_sites = settings.TRUSTEDHTML_CUT_SITES
        if cut_schemes is None:
            cut_schemes = settings.TRUSTEDHTML_CUT_SCHEMES
        if verify_sites is None:
            verify_sites = settings.TRUSTEDHTML_VERIFY_SITES
        if verify_schemes is None:
            verify_schemes = settings.TRUSTEDHTML_VERIFY_SCHEMES
        if verify_local is None:
            verify_local = settings.TRUSTEDHTML_VERIFY_LOCAL
        if local_sites is None:
            local_sites = settings.TRUSTEDHTML_LOCAL_SITES
        if local_schemes is None:
            local_schemes = settings.TRUSTEDHTML_LOCAL_SCHEMES
        self.type = type
        self.allow_sites = self.lower_list(allow_sites)
        self.allow_schemes = self.lower_list(allow_schemes)
        self.cut_sites = self.lower_list(cut_sites)
        self.cut_schemes = self.lower_list(cut_schemes)
        self.verify_sites = self.lower_list(verify_sites)
        self.verify_schemes = self.lower_list(verify_schemes)
        self.local_sites = self.lower_list(local_sites)
        self.local_schemes = self.lower_list(local_schemes)
        self.verify_local = verify_local

    @staticmethod
    def inlist(value, lst):
        """
        Check whether ``value`` is in ``lst``.
        All lists passed to this function can be:
            list of strings with allowed values.
            True to allow all values.
            False or None to disable all values
        If ``value`` is None than it is empty list.
        """
        if value is None:
            return True
        if lst is True:
            return True
        if lst is None or lst is False:
            return False
        return value in lst

    def preprocess(self, value, path):
        """
        Correct escaped-chars (%hh).
        We don`t replace escaped-chars, just replace "%Z" with "%25Z".
        Escaped-chars not allowed in scheme and authority paths,
        so we can trust prepared values.
        """
        value = super(Uri, self).preprocess(value, path)
        value = urlfix(value)
        return value

    def core(self, value, path):
        """Do it."""
        value = String.core(self, value, path)
        scheme_source, authority_source, path, query, fragment = urlsplit(value)
        scheme = self.lower_string(scheme_source)
        authority = self.lower_string(authority_source)
        if self.inlist(scheme, self.cut_schemes) and self.inlist(authority, self.cut_sites) and (
                scheme is not None or authority is not None):
            scheme = None
            authority = None
            if not path and not query and not fragment:
                path = '/'
        if not self.inlist(scheme, self.allow_schemes) or not self.inlist(authority, self.allow_sites):
            raise IncorrectException(self, value)
        if scheme is None:
            check_scheme = 'http'
        else:
            check_scheme = scheme
        if self.inlist(scheme, self.local_schemes) and self.inlist(authority, self.local_sites):
            if self.verify_local is True:
                if not path and query is not None:
                    raise IncorrectException(self, value)
                if path and not local_check(path, query):
                    raise IncorrectException(self, value)
            elif self.verify_local is not False:
                check = urljoin(check_scheme, self.verify_local, path, query, fragment)
                if not remote_check(check):
                    raise IncorrectException(self, value)
        elif self.inlist(scheme, self.verify_schemes) and self.inlist(authority, self.verify_sites):
            if authority is not None:
                check = urljoin(check_scheme, authority, path, query, fragment)
                if not remote_check(check):
                    raise IncorrectException(self, value)
        value = urljoin(scheme, authority, path, query, fragment)
        return value


class No(Rule):
    """
    Rule suppose that value never is correct.
    Validation always will raise IncorrectException.
    """

    def core(self, value, path):
        """Do it."""
        raise IncorrectException(self, value)


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
    If rule raise ElementException it will be immediately raised.
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
            except ElementException, exception:
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

    def __init__(
            self, rule, regexp=r'\s+', flags=0, min_split=0, max_split=0,
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
        if values:
            value = self.prepend_string + self.join_string.join(values) + self.append_string
        else:
            value = u''
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
        
        Return correct list of parts of value or raise IncorrectException or ElementException.
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
        except ElementException, exception:
            raise exception
        except TrustedException:
            return self.complex(values, path, value_index, rule_index + 1)


class Validator(object):
    """
    Provide mechanism to validate list of values (tag attributes or style properties)
    by corresponding rules.
    """

    def __init__(self, rules):
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
        Or raise exceptions.
        """
        if not self.rules:
            return []
        correct = {}
        source = {}
        for name, value in values:
            name = name.lower()
            source[name] = value
        for name, rule in self.rules.iteritems():
            try:
                name = name.lower()
                value = source.get(name, None)
                correct[name] = rule.validate(value, path)
            except ElementException, exception:
                raise exception
            except TrustedException:
                pass
        # Order values is source ordering. New values will be appended.
        order = [name.lower() for name, value in values]
        append = [name for name, value in correct.iteritems() if name not in order]
        order.extend(append)
        values = [(order.index(name), name, value) for name, value in correct.iteritems()]
        values.sort()
        return [(name, value) for index, name, value in values]


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
        Sequence.__init__(
            self, rule=None, regexp=r'\s*;\s*',
            join_string='; ', append_string=';', **kwargs)
        Validator.__init__(self, rules=rules)

    def preprocess(self, value, path):
        """Do it."""
        value = super(Style, self).preprocess(value, path)
        value = get_style(value)
        return value

    def sequence(self, values, path):
        """Do it."""
        properties = []
        for value in values:
            if ':' not in value:
                continue
            property_name = value[:value.find(':')].strip()
            property_value = value[value.find(':') + 1:].strip()
            properties.append((property_name, property_value))
        properties = self.check(properties, path)
        return [
            '%s: %s' % (property_name, property_value)
            for property_name, property_value in properties]


class Element(Rule, Validator):
    """
    Rule suppose that value is correct if ``value`` is LIST OF PAIRS
    (attribute_name, attribute_value) and each attribute_name
    has valid attribute_value corresponding to ``rules`` dictionary.
    Validation will return list of valid pairs (attribute_name, attribute_value).
    """

    def __init__(
            self, rules=None, contents=None, empty_element=False,
            remove_element=False, optional_start=False, optional_end=False,
            save_content=True, **kwargs):
        """
        ``rules`` is dictionary in witch key is name of property
        (or tag attribute) and value is corresponding rule.
        
        ``contents`` list of elements allowed inside this one.
        List contains strings with names or True to allow text content.
        
        ``empty_element`` where element can contain no content.
        
        ``remove_element`` where element must be removed in any case.

        ``optional_start`` start of this element is optional.

        ``optional_end`` end of this element is optional.
        
        ``save_content`` whether content of incorrect tag must be saved
        to parent tag. 
        """
        if rules is None:
            rules = {}
        if contents is None:
            contents = []
        Rule.__init__(self, **kwargs)
        Validator.__init__(self, rules=rules)
        self.contents = contents
        self.empty_element = empty_element
        self.remove_element = remove_element
        self.optional_start = optional_start
        self.optional_end = optional_end
        self.save_content = save_content
        if self.contents is None:
            self.empty_element = True

    def preprocess(self, value, path):
        """Do it."""
        # Don`t call super to avoid raise EmptyException
        value = [
            (attribute_name, get_cdata(attribute_value))
            for attribute_name, attribute_value in value]
        return value

    def postprocess(self, value, path):
        """Do it."""
        # Don`t call super to avoid raise EmptyException
        return value

    def core(self, value, path):
        """Do it."""
        try:
            return self.check(value, path)
        except ElementException, exception:
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
        ('&', '&amp;'),  # Must be first element in list
        ('"', '&quot;'),
        ("'", '&apos;'),
        ('<', '&lt;'),
        ('>', '&gt;'),
        #(NBSP_CHAR, NBSP_TEXT),
    ]
    PLAIN_CHARS = [SPECIAL_CHARS[index] for index in range(len(SPECIAL_CHARS) - 1, -1, -1)]
    CODE_RE = re.compile('&#(([0-9]+);?|x([0-9A-Fa-f]+);?)')
    CODE_RE_SPECIAL = dict(
        [(0, '')] + [(ord(char), string) for char, string in SPECIAL_CHARS])
    SYSTEM_RE = re.compile('[\x01-\x1F\s]+')

    NBSP_CHAR = u'\xa0'
    NBSP_TEXT = '&nbsp;'
    NBSP_RE = re.compile('[' + NBSP_CHAR + ' ]{2,}')

    DEFAULT_ROOT_TAG = 'p'

    MARKUP_MASSAGE = BeautifulSoup.MARKUP_MASSAGE + [
        (re.compile('<!-([^-])'), lambda match: '<!--' + match.group(1))
    ]

    BEAUTIFUL_SOUP = BeautifulSoup()

    def __init__(
            self, rules, fix_number=2, prepare_number=2, root_tags=None,
            allow_empty=True, **kwargs):
        """
        ``rules`` is dictionary in witch key is name of property
        (or tag attribute) and value is corresponding rule.
        
        ``fix_number`` specified number of maximum attempts to fix value.

        ``prepare_number`` specified number of maximum attempts to prepare value.

        ``root_tags`` list of tags that can be in the root of document.
        """
        if root_tags is None:
            root_tags = []
        super(Html, self).__init__(allow_empty=allow_empty, **kwargs)
        self.rules = rules
        self.fix_number = fix_number
        self.prepare_number = prepare_number
        self.root_tags = root_tags
        if self.DEFAULT_ROOT_TAG not in self.root_tags:
            self.root_tags.append(self.DEFAULT_ROOT_TAG)

    def remove_spaces(self, value):
        """Removes spaces from ``value``"""
        return self.NBSP_RE.sub(self.NBSP_CHAR, value)

    def correct(self, value):
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
                    tag = soup.contents[index]
                    if rule is None:
                        raise IncorrectException(self, tag.attrs)
                    if rule.remove_element:
                        raise IncorrectException(self, tag.attrs)
                    tag.attrs = rule.validate(tag.attrs, path)
                except TrustedException:
                    element = soup.contents[index].extract()
                    if rule is None or getattr(rule, 'save_content', True):
                        insert = index
                        while len(element.contents):
                            soup.insert(insert, element.contents[0])
                            insert += 1
                    continue
                self.clear(soup.contents[index], path)
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
            index += 1
        return soup

    def join(self, soup):
        changed = False
        index = 0
        while index < len(soup.contents) - 1:
            if (
                    not isinstance(soup.contents[index + 1], Tag)
                    and not isinstance(soup.contents[index], Tag)):
                text = soup.contents[index].string + soup.contents[index + 1].string
                text = self.correct(text)
                if text != soup.contents[index].string:
                    soup.contents[index].replaceWith(text)
                soup.contents[index + 1].extract()
                changed = True
                continue
            index += 1
        return changed

    def collapse(self, soup):
        changed = True
        while changed:
            changed = False
            index = 0
            while index < len(soup.contents):
                if isinstance(soup.contents[index], Tag):
                    self.collapse(soup.contents[index])
                    if not self.BEAUTIFUL_SOUP.isSelfClosingTag(soup.contents[index].name):
                        text = soup.contents[index].renderContents(encoding=None)
                        # encoding=None: Fix bug in BeautifulSoup (don`t work with unicode)
                        text = self.correct(text)
                        if not text or text == ' ' or text == self.NBSP_CHAR:
                            rule = self.rules[soup.contents[index].name]
                            if rule.default and text != rule.default:
                                changed = True
                                text = rule.default
                                while soup.contents[index].contents:
                                    soup.contents[index].contents[0].extract()
                                soup.contents[index].append(text)
                            else:
                                if not rule.empty_element:
                                    changed = True
                                    if text:
                                        soup.contents[index].replaceWith(text)
                                    else:
                                        soup.contents[index].extract()
                                        continue
                index += 1
            if not changed:
                if self.join(soup):
                    changed = True
        return soup

    def collapse_root(self, soup):
        index = 0
        while index < len(soup.contents):
            if not isinstance(soup.contents[index], Tag):
                text = soup.contents[index].string
                text = self.correct(text)
                if not text or (text == ' ') or (text == self.NBSP_CHAR):
                    soup.contents[index].extract()
                    continue
            index += 1
        return soup

    def need_wrap(self, content, for_next):
        if isinstance(content, Tag):
            if content.name in self.root_tags:
                return False
        else:
            if not for_next and (
                    content.string == ''
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
        soup = BeautifulSoup(
            value, markupMassage=self.MARKUP_MASSAGE,
            convertEntities=BeautifulSoup.ALL_ENTITIES)
        soup = self.clear(soup, path)
        soup = self.collapse(soup)
        soup = self.collapse_root(soup)
        soup = self.wrap(soup)
        return unicode(soup)

    def core(self, value, path):
        """Do it."""
        path = path[:] + [self]
        value = String.core(self, value, path)
        for iteration in xrange(self.fix_number + 1):
            for preparing in xrange(self.prepare_number + 1):
                source = value
                value = self.correct(value)
                if source == value:
                    break
            else:
                raise IncorrectException(self, 'Too much attempts to prepare value')
            source = value
            value = self.fix(value, path)
            if source == value:
                break
        else:
            raise IncorrectException(self, 'Too much attempts to fix value')
        return value
