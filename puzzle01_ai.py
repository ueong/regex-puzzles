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
