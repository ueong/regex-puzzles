import re

txt = """
expurgatory xylometer yex xenomorphically exquisitely
xylology xiphosurans xenophile yunx oxytocin xylogen
xeriscapes xerochasy inexplicably yonderly inexpressibly
extremity xerox xiphophyllous xylographic complexly vexillology
xanthenes xylenol xylol yexing xylenes coextensively
"""
pat6 = re.compile(r'\b[xy][a-z]*[xy]\b')
print(re.findall(pat6, txt))

pat7 = re.compile(r'\b((x[a-z]*y)|(y[a-z]*x))\b')
print([m[0] for m in re.findall(pat7, txt)])