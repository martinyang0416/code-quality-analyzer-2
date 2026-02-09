import sys
from collections import deque

def string_to_int(s):
    res = 0
    for i in range(len(s)):
        if s[i] == '1':
            res += (1 << i)
    return res

def rotate_right(s, n):
    if n == 0:
        return s
    last_bit = (s >> (n-1)) & 1
    rotated = (s << 1) % (1 << n) | last_bit
    return rotated

def solve():
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    N = int(input[idx])
    idx += 1
    
    for _ in range(T):
        lig