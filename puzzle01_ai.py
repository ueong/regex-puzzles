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

# Find all and only words that start with x and end with y. Show me the python program for that.

import re

pattern = r"\bx\w+y\b"

words = re.findall(pattern, txt)

print(words)

txt2 = "breathiness xenogeny randed xyxyblah xylotomy"
words2 = re.findall(pattern, txt2)

print(words2)

# Find all and only lowercase words that start with x and end with y. Show me the python program for that.
import re

text = "Example text with xylophone and Xylography."
pattern = r"\bx\w+y\b" 

matches = re.findall(pattern, text)
print(matches)
