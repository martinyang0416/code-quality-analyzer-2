def main():
    import sys
    s = sys.stdin.read().strip()

    target = list("bessie")
    m = len(target)
    n = len(s)
    dp = [0] * (m + 1)
    dp[0] = 1
    cnt_6 = []
    for c in s:
        new_dp = dp.copy()
        for j in range(m-1, -1, -1):
            if c == target[j]:
                new_dp[j+1] += dp[j]
        dp = new_dp
        cnt_6.append(dp[m])
    
    first_total = 0
    for i in range(n):
        first_total += (i + 1) * cnt_6[i]
    
    S = [0] * n
    for i in rang