import re

# Write a python program that returns count of specific string pattern within a string. It should use regular expressions.
s = """If I'm butter, if I'm butter
If I'm butter, then he's a hot knife
He makes my heart a CinemaScope screen
Showing the dancing bird of paradise
"""

def count_substring(pattern, string):
  return len(re.findall(pattern, string))

print(count_substring("e", s))
print(count_substring('tt', s))
