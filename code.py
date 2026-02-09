import sys
sys.setrecursionlimit(1 << 25)

def pow_less(a, b, limit):
    res = 1
    for _ in range(b):
        res *= a
        if res >= limit:
            return False
    return res < limit

memo = {}

def can_win(a, b, n):
    key = (a, b)
    if key in memo:
        return memo[key]
    
    move_a_valid = pow_less(a + 1, b, n)
    move_b_valid = pow_less(a, b + 1, n)
    
    if not move_a_valid and not move_b_valid:
        memo[key] = False
        return False
    
    result = False
