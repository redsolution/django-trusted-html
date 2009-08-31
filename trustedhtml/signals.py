"""
rule_done
    This signal is sent when value successfully passed the rule.
    Arguments sent with this signal:
        sender - class of the rule
        rule - instance of the rule
        value - instance of the value
        state - extended information passed by the rule.

rule_exception
    This signal is sent when value fail to pass the rule.
    Arguments sent with this signal:
        sender - class of the rule
        rule - instance of the rule
        value - instance of the value
        exception - raised exception
"""

from django.dispatch import Signal

rule_done = Signal(providing_args=['rule', 'parent', 'value', 'state', ])

rule_exception = Signal(providing_args=['rule', 'parent', 'value', 'state', 'exception', ])
