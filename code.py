def countNumbers(digits, n):
    s = str(n)
    k = len(s)
    sum_less = sum(len(digits) ** m for m in range(1, k))
    digits_sorted = sorted(digits)
    
    from functools import lru_cache
    
    @lru_cache(maxsize=None)
    def dp(pos, tight):
        if pos == k:
            return 1
        limit = s[pos] if tight else '9'
        count = 0
        for d in digits_sorted:
            if d > limit:
                continue
            new_tight = tight and (d == limit)
            if new