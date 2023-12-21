import re

valid = "LuHHHdLuHFLLLFHdLLLLFHHdLLu"
valid2 = "LLLLuHHHHHH"
invalid = "LHuHHHuLLdL"
invalid2 = "FduF"
invalid3 = "LLuHHFLLXLLu"

# Write a Python function to identify whether a string matches a pattern. The pattern must have cach L followed by L, u, or F. The pattern must have each U followed by U, d, or F. The pattern must have each u followed by U. The pattern must have each d followed by L. The pattern must have each F followed by L or U. All other patterns are prohibited. Use regular expressions to give a more compact solution.
def check_pattern(string):
  pat = r"^(((?=LL|Lu|LF|HH|Hd|HF|uH|dL|FH|FL)|(?=.$))[LHudF])+$"
  if re.search(pat, string):
    return "Matches pattern"
  else:
    return "Does not match pattern"

print(check_pattern(valid))
print(check_pattern(valid2))
print(check_pattern(invalid))
print(check_pattern(invalid2))
print(check_pattern(invalid3))

