import re

def is_something(s):
    return re.match(r'^(.+?)\1+$', s)

# Recommend proper name of this function.
# def is_something(s): return re.match(r'^(.+?)\1+$', s)

# has_repeated_section
# contains_repeated_substring
# matches_repeated_pattern

