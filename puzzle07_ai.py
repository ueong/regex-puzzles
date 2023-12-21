import re

good = '{1:3}{3:3}{3:6}{6:1}{1:3}{3:3}{3:3}'
bad = '{1:3}{3:3}{6:1}{1:3}{3:3}{3:6}{3:3}'
awful = '{1:3}{{3:5}}{5:2}'

pat = r'^(({[1-6]:([1-6])})(?=$|{\3))+$'

# Match a pattern where adjacent numbers, between bracketed pairs, are the same. For example, good: "{1:3}{3:3}{3:6}{6:1}{1:3}{3:3}{3:3}" and bad "{1:3}{3:3}{6:1}{1:3}{3:3}{3:6}{3:3}". The pattern is a string of numbers, separated by colons, between brackets.
pattern = r'\{(\d+):(\d+)\}(?:\{\2:\2\})*'

for play in (good, bad, awful):
    match = re.search(pattern, play)
    if match:
        print(match.group(), "wins!")
    else:
        print(play, "loses!")

# Match a pattern of dominoes in a linear row.
domino_string = "{1:3}{3:3}{3:6}{6:1}{1:3}{3:3}{3:3}"

pattern = r"\{(\d+):(\d+)\}(?:\{\2:\2\})*"

match = re.search(pattern, awful)

if match:
  print(awful, "matches the pattern")
else: 
  print(awful, "does not match the pattern")
