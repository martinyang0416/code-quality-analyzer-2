groups = [
    ['a', 'b', 'c', 'd', 'e'],
    ['f', 'g', 'h', 'i', 'j'],
    ['k', 'l', 'm', 'n', 'o'],
    ['p', 'q', 'r', 's', 't'],
    ['u', 'v', 'w', 'x', 'y'],
    ['z', '.', '?', '!', ' ']
]

def convert(s):
    if len(s) % 2 != 0:
        return "NA"
    res = []
    for i in range(0, len(s), 2):
        pair = s[i:i+2]
        if len(pair) != 2:
            return "NA"
        a, b = pair[0], pair[1]
        if a not in '123456' or b not in '12345':
            return "NA"
        group