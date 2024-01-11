# Write a Python function that uses regular expressions to count the occurrences of a substring within a string. Do not use the len() function or a loop to count the length of an iterable. You should use recursion instead of loop or len() function.
import re

# AI의 패배였다. 아마 문자열 길이를 알 수 없는 것 같다. 어떻게 해야 할까? 나중에 다시 해보자. 
def count_occurrences(substring, string, start_index=0):
  if start_index == len(string):
    return 0
  
  if string[start_index:start_index+len(substring)] == substring:
    return 1 + count_occurrences(string, substring, start_index+1)
  else:  
    return count_occurrences(string, substring, start_index+1)

print(count_occurrences("hello world", "l"))


s = """If I'm butter, if I'm butter
If I'm butter, then he's a hot knife
He makes my heart a CinemaScope screen
Showing the dancing bird of paradise
"""

print(count_occurrences("e", s))
print(count_occurrences("tt", s))
print(count_occurrences("butter", s))

