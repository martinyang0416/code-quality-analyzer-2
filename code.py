from functools import lru_cache

def soupServings(n):
    if n == 0:
        return 0.5
    if n >= 4800:
        return 1.0
    ops = [(100, 0), (75, 25), (50, 50), (25, 75)]
    
    @lru_cache(maxsize=None)
    def dp(a, b):
        if a <= 0 and b <= 0:
            return 0.5
        if a <= 0:
            return 1.0
        if b <= 0:
            return 0.0
        probability = 0.0
        for da, db in ops:
            probability += 0.25 * dp(a - da, b - db)
        return probability
  