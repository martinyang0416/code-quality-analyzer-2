def splitArraySameAverage(A):
    n = len(A)
    if n == 1:
        return False
    total_sum = sum(A)
    dp = [set() for _ in range(n + 1)]
    dp[0].add(0)
    for num in A:
        for k in range(n - 1, -1, -1):
            if dp[k]:
                for s in dp[k]:
                    dp[k + 1].add(s + num)
    for k in range(1, n):
        if (total_sum * k) % n != 0:
            continue
        target = (total_sum * k) // n
        if target in dp[k]:
            return True
    return F