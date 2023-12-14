
# convert the text in the 'config' variable to a dictionary mapping the numbers to the left of the equal sign to the strings to the right. Write a python program for it.
## 첨에 에러가 났다.
# import re

# config = """
# 3 = foobar 
# 14=baz
# 9= fizzbuzz
# 21=more_stuff,here
# """

# dict = {}
# pairs = re.split(r"\s*=\s*", config) 

# for pair in pairs:
#   key, value = pair.split() 
#   dict[key] = value

# print(dict)

import re

config = """
3 = foobar
14=baz  
9=fizzbuzz
21=more_stuff,here
"""

dict = {}
pairs = re.split(r"\s*=\s*", config)
for pair in pairs:
   key, value = pair.split('=')
   dict[key] = value

print(dict)


# I got this error!! Fix it! key, value = pair.split()ValueError: not enough values to unpack (expected 2, got 1)
# config = """
# 3 = foobar
# 14=baz 
# 9=fizzbuzz
# 21=more_stuff,here
# """

# dict = {}
# pairs = re.split(r"\s*=\s*", config)

# for pair in pairs:
#   parts = pair.split(maxsplit=1)
#   key = parts[0]
#   value = parts[1] if len(parts) > 1 else ""
#   dict[key] = value

# print(dict)

# 하하하. 이렇게 잘못된 결과를 내놓았다. 
# {'3': '', 'foobar': '14', 'baz': '9', 'fizzbuzz': '21', 'more_stuff,here': ''}

# import re

# config = """
# 3 = foobar
# 14=baz  
# 9=fizzbuzz
# 21=more_stuff,here 
# """

# dict = {}
# pairs = re.split(r"\s*=\s*", config)

# for pair in pairs:
#   key, value = pair.split(maxsplit=1)
#   dict[key] = value

# print(dict)
# import re

# config = """
# 3 = foobar
# 14=baz  
# 9=fizzbuzz
# 21=more_stuff,here 
# """
# dict = {}
# pairs = re.split(r"\s*=\s*", config)

# 또 틀린 답
# for pair in pairs:
#   parts = pair.split(maxsplit=1) 
#   if len(parts) > 1:
#     key = parts[0] 
#     value = parts[1]
#   else:
#     continue

#   dict[key] = value
# for pair in pairs:
#   parts = pair.split(maxsplit=1)
#   key = parts[0]
#   value = parts[1] if len(parts) > 1 else ""

#   dict[key] = value

# print(dict)
