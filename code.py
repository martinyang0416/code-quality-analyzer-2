def minNumberOfFrogs(croakOfFrogs):
    counts = {'c': 0, 'r': 0, 'o': 0, 'a': 0}
    max_frogs = 0
    for char in croakOfFrogs:
        if char == 'c':
            counts['c'] += 1
        elif char == 'r':
            if counts['c'] == 0:
                return -1
            counts['c'] -= 1
            counts['r'] += 1
        elif char == 'o':
            if counts['r'] == 0:
                return -1
            counts['r'] -= 1
            counts['o'] += 1
        elif char == 'a':
     