import re
from datetime import datetime

# U+25A0 ■
# U+25AA ▪
# U+25CB ○
# U+25C9 ◉
# U+25A1 □
# U+25AB ▫
# U+25B2 ▲
# U+25CF ●
# U+2404 ␄

# Check whether a string alternates between r'[■▲○◉□]+' and r'[▫□▪●▲]+' then ends with r'␄'. Write a python program for that.
def check_pattern(text):
    pattern = r'([■▲○◉□]+)[▫□▪●▲]+([■▲○◉□]+)[▫□▪●▲]+␄'
    match = re.fullmatch(pattern, text)
    if match:
        print("Pattern matched") 
    else:
        print("Pattern not matched")

# check_pattern("■▲○▫□␄") # Pattern not matched
# check_pattern("■▲○◉□▪●▲■▲␄") # Pattern matched

pattern = re.compile(r'(^(([■▲○◉□]+) ?([▫□▪●▲]+) ?)+)␄')
pattern2 = re.compile(r'(^(?=^[■▲○◉□▫▪●]+␄)(([■▲○◉□]+) ?([▫□▪●▲]+) ?)+)␄')
structure_1212 = "■▲◉▫■▪▫␄"
quick_match = "■▲○◉□▫□▪●◉◉▫▪▪●●□□▲▲○○◉■◉■▲▲□□◉▲␄"
missing_terminator = "■▲◉▫■▪▫"
slow_failure = "▲□□▲▲▲□□▲▲▲□□□□□□□□▲▲□▲□▲□▲X"
one_more_symbol = "▲▲▲▲□▲□□▲▲□▲□□□□□□□□▲▲□▲□▲□▲▲"
# match = re.findall(pattern, quick_match)
# print(match)

# print(re.findall(pattern, structure_1212))
# print(re.findall(pattern, missing_terminator))
start_time = datetime.now()
# print(re.findall(pattern, slow_failure))
# print(re.findall(pattern2, one_more_symbol))
# check_pattern(one_more_symbol)
check_pattern(quick_match)
check_pattern(structure_1212)
check_pattern(missing_terminator)
check_pattern(slow_failure)
end_time = datetime.now()
print("Execution time:", end_time - start_time)
