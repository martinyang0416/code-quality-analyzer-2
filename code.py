import sys

def compute(s):
    target = ['b', 'e', 's', 's', 'i', 'e']
    count = [0] * 7
    total = 0
    for c in s:
        new_count = [0] * 7
        # Handle new substrings starting at current character
        if c == target[0]:
            new_count[1] += 1
        else:
            new_count[0] += 1
        # Process previous counts
        for i in range(7):
            if count[i] > 0:
                new_count[i] += count[i]
                if c == target[i]:
                    n