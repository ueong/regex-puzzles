import re

config = """
3 = foobar
14=baz
9= fizzbuzz
21=more_stuff,here
"""

print(dict(re.findall(r'(\d+) *= *(.*)$', config, re.MULTILINE)))

print({int(k): v for k, v in re.findall(r'(\d+) *= *(.*)$', config, re.MULTILINE)})