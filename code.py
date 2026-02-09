import math

def max_sum_after_flips(t, test_cases):
    results = []
    for case in test_cases:
        n, m, a, B = case
        sum_initial = sum(a)
        sum_abs = sum(abs(num) for num in a)
        B = set(B)
        
        if 1 in B:
            results.append(sum_abs)
            continue
        
        has_odd = any(x % 2 != 0 for x in B)
        if has_odd:
            results.append(sum_abs)
            continue
        
        negatives = [num for num in a if num < 0]
        