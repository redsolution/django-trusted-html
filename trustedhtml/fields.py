# -*- coding: utf-8 -*-

from django import forms

from trustedhtml.classes import TrustedHtml
from trustedhtml.rules import html

class TrustedHtmlField(forms.CharField):
    """Use max_length to avoid expensing CPU and MEM resources"""
    
    def clean(self, value):
        value = TrustedHtml(value, trusted_dictionary=html).html
        return super(_ArticleCharField, self).clean(value)
