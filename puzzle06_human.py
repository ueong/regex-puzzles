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
print(re.findall(pattern2, one_more_symbol))
end_time = datetime.now()
print("Execution time:", end_time - start_time)
