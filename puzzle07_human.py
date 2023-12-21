import re

good = '{1:3}{3:3}{3:6}{6:1}{1:3}{3:3}{3:3}'
bad = '{1:3}{3:3}{6:1}{1:3}{3:3}{3:6}{3:3}'
awful = '{1:3}{{3:5}}{5:2}'

pat = r'^(({[1-6]:([1-6])})(?=$|{\3))+$'

for play in (good, bad, awful):
    match = re.search(pat, play)
    if match:
        print(match.group(), "wins!")
    else:
        print(play, "loses!")

