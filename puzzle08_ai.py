# Write a Python program that identifies whether a string is valid. The alphabet is ABCD. In a valid string, A may be followed B or C. B may be followed by B or C. C may be followed by D. And D may be followed by A. All other strings are invalid.
import re

pat = r"^(A(?=$|[BC])|B(?=$|[BC])|C(?=$|D)|D(?=$|A))+$"

strings = ["ABCD", "ABCB", "ABDABCB", "ABCDE", "ABCDABB", "ABCDABCDABCDA"]

for s in strings:
  if re.search(pat, s):
    print(f"{s} is valid")
  else: 
    print(f"{s} is invalid")
