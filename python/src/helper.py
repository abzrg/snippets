"""A simple helper module"""

_debug: bool = False


def set_debug(value):
    """Set the helper's debug switch"""
    global _debug
    _debug = value


def get_debug():
    """Get the sate of debugging switch"""
    global _debug
    return _debug


def p(*args, **kwargs):
    """Having things printed with less typing"""
    global _debug
    if _debug:
        print(*args, **kwargs)
