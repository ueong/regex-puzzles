import re

win = 'ABCDABB'
lose = 'ABDABCB'
win2 = 'ABCDABCDABCDA'

pat = r'^(A(?=$|[BC])|B(?=$|[BC])|C(?=$|D)|D(?=$|A))+$'
print(re.search(pat, win))
print(re.search(pat, lose) or "No Match")
print(re.search(pat, win2) or "No Match")