def is_non_decreasing(s):
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            return False
    return True

def is_non_increasing(s):
    for i in range(len(s) - 1):
        if s[i] < s[i + 1]:
            return False
    return True

s = input().strip()
even = s[::2]  # Characters at even indices
odd = s[1::2]  # Characters at odd indices

even_nd = is_non_decreasing(even)
even_ni = is_non_increasing(even)
odd_nd = is_non_decreasing(odd)
odd_ni = is_non_increasing(odd)

# C