import re
counter = {
    r'(^@*)(_________)(.*$)': r'\g<1>9\g<3>',
    r'(^@*)(________)(.*$)': r'\g<1>8\g<3>',
    r'(^@*)(_______)(.*$)': r'\g<1>7\g<3>',
    r'(^@*)(______)(.*$)': r'\g<1>6\g<3>',
    r'(^@*)(_____)(.*$)': r'\g<1>5\g<3>',
    r'(^@*)(____)(.*$)': r'\g<1>4\g<3>',
    r'(^@*)(___)(.*$)': r'\g<1>3\g<3>',
    r'(^@*)(__)(.*$)': r'\g<1>2\g<3>',
    r'(^@*)(_)(.*$)': r'\g<1>1\g<3>',
    r'(^@*)(_*)(.*$)': r'\g<1>0\g<3>'
}
def let_count(c: str, s: str) -> int:
    s = re.sub(fr'{c}', '_', s)
    s = re.sub(fr'[^_]', '', s)

    while True:
        s = re.sub(r'__________', '@', s)
        for k, v in counter.items():
            new = re.sub(k, v, s)
            if new != s:
                s = new
                print(s)
                break

        if re.match(r'^[0-9]*$', s):
            return s
        s = re.sub('@', '_', s)

s = """If I'm butter, if I'm butter
If I'm butter, then he's a hot knife
He makes my heart a CinemaScope screen
Showing the dancing bird of paradise
"""

print(let_count("e", s))
print(let_count("tt", s))
# print(let_count("butter", s))