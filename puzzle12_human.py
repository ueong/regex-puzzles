import re

# def is_something(s):
#    return re.match(r'^(.+?)\1+$', s)

def repeated_prefix(s):
    """ Look for any prefix string in 's' and match only if
    that prefix is repeated at least once, but it might be
    repeated many times. No other substring may occur between
    the start and end of the string for a match.
    """
    return re.match(r'^(.+?)\1+$', s)
