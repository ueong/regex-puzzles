import re

txt = """
expurgatory xylometer yex xenomorphically exquisitely
xylology xiphosurans xenophile yunx oxytocin xylogen
xeriscapes xerochasy inexplicably yonderly inexpressibly
extremity xerox xiphophyllous xylographic complexly vexillology
xanthenes xylenol xylol yexing xylenes coextensively
"""
# Identify *both* words that start with 'x' and end with 'y', but *also* the words that start with 'y' and end with 'x'. Write a python program for it.
import re

pattern1 = r"\bx\w+y\b"
pattern2 = r"\by\w+x\b"

words = re.findall(pattern1, txt) + re.findall(pattern2, txt)

print(words)

# Identify *both* words that start with 'x' and end with 'y', but *also* the words that start with 'y' and end with 'x'. Write a python program for it. You can use only one regex pattern for it.
import re

pattern = r"(?:\bx\w+y\b|\by\w+x\b)"

print(re.findall(pattern, txt))

# Write a Python program to identify both words that start with x and end with y and also words that start with y and end with x, within a paragraph of text, using regular expressions.
import re

pattern = r"(?:\bx\w+y\b|\by\w+x\b)"

print(re.findall(pattern, txt))
