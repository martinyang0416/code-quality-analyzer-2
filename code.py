def find_kth_smallest(n, m, k):
    def count(mid):
        total = 0
        x = mid // m
        total += x * m
        i = x + 1
        while i <= n:
            q = mid // i
            if q == 0:
                break
            max_i = mid // q
            if max_i > n:
                max_i = n
            total += q * (max_i - i + 1)
            i = max_i + 1
        return total
    
    low = 1
    high = n * m
    while low < high:
        mid = (low + high) // 2
        if count(mi