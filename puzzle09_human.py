import re

valid = "LuHHHdLuHFLLLFHdLLLLFHHdLLu"
valid2 = "LLLLuHHHHHH"
invalid = "LHuHHHuLLdL"
invalid2 = "FduF"
invalid3 = "LLuHHFLLXLLu"

pat = (r'^(((?=LL|Lu|LF|HH|Hd|HF|uH|dL|FH|FL)|(?=.$))[LHudF])+$')
print(re.search(pat, valid))
print(re.search(pat, valid2))
print(re.search(pat, invalid))
print(re.search(pat, invalid2))
print(re.search(pat, invalid3))



