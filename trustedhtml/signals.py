"""
``rule_done`` signal is sent when value successfully passed the rule.
    ``sender`` - class of the rule
    ``rule`` - instance of the rule
    ``value`` - instance of the value
    ``source`` - instance of value`s source variant
Receiver functions must return correct value or raise TrustedException.
Returned value will be used as result of validation.
If more than one signals will be used than all signals will get source value
but only result of last signal will be used as result of validation.

``rule_exception`` signal is sent when value fail to pass the rule.
    ``sender`` - class of the rule
    ``rule`` - instance of the rule
    ``value`` - instance of the value
    ``source`` - instance of value`s source variant
    ``exception`` - raised exception
"""

from django.dispatch import Signal

rule_done = Signal(providing_args=['rule', 'parent', 'value', 'source', ])

rule_exception = Signal(providing_args=['rule', 'parent', 'value', 'source', 'state', 'exception', ])
