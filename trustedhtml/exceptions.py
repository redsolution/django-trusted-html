# -*- coding: utf-8 -*-

class TrustedException(ValueError):
    u"""
    Base trustedhtml exception.
    """
    pass

class RequiredException(TrustedException):
    u"""
    Raised when value is absent and required flag is True. 

    Example: src attribute for <img />
    """
    pass
 
class InvalidException(TrustedException):
    u"""
    Raised when value pass check and invalid flag is True.
    
    Example: "none" value for "display" style property (we want to remove such tag)
    """
    pass
    
class EmptyException(TrustedException):
    u"""
    Raised when value is empty and allow_empty is False.

    Example: width attribute for <div />
    """
    pass
 
class DefaultException(TrustedException):
    u"""
    Raised when value is empty and default value is not None. 
    
    Example: alt attribute for <img />
    """
    pass
    
class SequenceException(TrustedException):
    u"""
    Raised when element to corresponded to sequence. 
    
    Example: color is not specified for "border" style property
    """
    pass
 
