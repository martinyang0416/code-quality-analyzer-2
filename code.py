import sys
from functools import lru_cache

def main():
    N = sys.stdin.readline().strip()
    K = int(sys.stdin.readline())
    digits = list(map(int, N))
    n = len(digits)

    @lru_cache(maxsize=None)
    def dp(pos, tight, leading_zero, cnt):
        if pos == n:
            return 0 if leading_zero else (1 if cnt == K else 0)
        res = 0
        max_d = digits[pos] if tight else 9
        for d in range(0, max_d + 1):
            new_tight = tight and (d == max_d)
            new_le