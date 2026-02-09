n = int(input())

def left_rotate_1(s):
    if len(s) <= 1:
        return s
    return s[1:] + s[0]

def right_rotate_1(s):
    if len(s) <= 1:
        return s
    return s[-1] + s[:-1]

def swap_halves(s):
    n = len(s)
    if n % 2 == 0:
        mid = n // 2
        return s[mid:] + s[:mid]
    else:
        mid = n // 2
        return s[mid+1:] + s[mid] + s[:mid]

def decrement_digits(s):
    res = []
    for c in s:
        if c.isdigit():
            res.append(str((int(c) - 1) % 10))
  