import re

txt = """
expurgatory xylometer xenotime xenomorphically exquisitely
xylology xiphosurans xenophile oxytocin xylogen
xeriscapes xerochasy inexplicably exabyte inexpressibly
extremity xiphophyllous xylographic complexly vexillology
xanthenes xylenol xylol xylenes coextensively
"""
# Find all words that start with 'x' and end with 'y' from above variable 'txt'. Write a python program for it.

import re

pattern = r"\bx\w+y\b"

print(re.findall(pattern, txt))

# Find all lowercase words that start with 'x' and end with 'y'. Write a python program for it.
import re

pattern = r"\bx\w+y\b" 

print(re.findall(pattern, txt))
