import re

def my_count(substring: str, string: str) -> int:
    return len(re.findall(substring, string))

s = """If I'm butter, if I'm butter
If I'm butter, then he's a hot knife
He makes my heart a CinemaScope screen
Showing the dancing bird of paradise
"""

print(my_count("e", s))
print(my_count('tt', s))

