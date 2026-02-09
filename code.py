def isInterleave(s1: str, s2: str, s3: str) -> bool:
    n, m = len(s1), len(s2)
    if n + m != len(s3):
        return False
    dp = [False] * (m + 1)
    dp[0] = True
    # Initialize first row (i=0)
    for j in range(1, m + 1):
        dp[j] = dp[j-1] and (s2[j-1] == s3[j-1])
    # Fill the DP table
    for i in range(1, n + 1):
        new_dp = [False] * (m + 1)
        # Handle j=0 case
        new_dp[0] = dp[0] and (s1[i-1] == s3[i-1])
        for j in range(1, m + 1):
            # Che