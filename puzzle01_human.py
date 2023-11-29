import re

txt = """
xenerthral xerically xenomorphically xebec xenomania
xenogenic xenogeny xenophobically xenon xenomenia
xylotomy xenogenies xenografts xeroxing xenons xanthous
xenoglossy xanthopterins xenoglossy xeroxed xenophoby
xenoglossies xanthoxyls xenoglossias xenomorphically
xeroxes xanthopterin xebecs xenodochiums xenodochium
xylopyrography xanthopteroins xerochasy xenium xenic
"""

pat1 = re.compile(r'x.*y')
xy_words1 = re.findall(pat1, txt)
print(xy_words1)

pat2 = re.compile(r'x.*?y')
xy_words2 = re.findall(pat2, txt)
print(xy_words2)

pat3 = re.compile(r'x[a-z]*y')
xy_words3 = re.findall(pat3, txt)
print(xy_words3)

txt2 = "breathiness xenogeny randed xyxyblah xylotomy"
xy_words4 = re.findall(pat3, txt2)
print(xy_words4)
