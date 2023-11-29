import re

txt = """
expurgatory xylometer xenotime xenomorphically exquisitely
xylology xiphosurans xenophile oxytocin xylogen
xeriscapes xerochasy inexplicably exabyte inexpressibly
extremity xiphophyllous xylographic complexly vexillology
xanthenes xylenol xylol xylenes coextensively
"""

pat3 = re.compile(r'x[a-z]*y')
xy_words3 = re.findall(pat3, txt)
print(xy_words3)

pat4 = re.compile(r'\bx[a-z]*y\b')
xy_words4 = re.findall(pat4, txt)
print(xy_words4)

pat5 = re.compile(r'(?<=^|(?<=[^a-z]))x[a-z]+y(?=$|[^a-z])')
print(re.findall(pat5, txt))
