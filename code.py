def largestNumber(cost, target):
    dp = [-float('inf')] * (target + 1)
    dp[0] = 0
    for i in range(1, target + 1):
        for j in range(9):
            c = cost[j]
            if i >= c and dp[i - c] + 1 > dp[i]:
                dp[i] = dp[i - c] + 1
    if dp[target] <= 0:
        return "0"
    
    res = []
    sum_remain = target
    digits_remain = dp[target]
    
    while digits_remain > 0:
        for d in range(8, -1, -1):
            digit = d + 1
            c = cost[d]
     