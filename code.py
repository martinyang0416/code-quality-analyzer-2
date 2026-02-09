MOD = 10**9 + 7

def distinctSubseqCount(s: str) -> int:
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    last_occurrence = {}
    for i in range(1, n + 1):
        c = s[i-1]
        dp[i] = (2 * dp[i-1]) % MOD
        if c in last_occurrence:
            dp[i] = (dp[i] - dp[last_occurrence[c] - 1]) % MOD
        last_occurrence[c] = i
    return (dp[n] - 1) % MOD