def compute(s):
    target = 'bessie'
    n = len(s)
    m = len(target)
    completions = []
    dp = [-1] * (m + 1)  # dp[0] is initialized to -1 (start), others to INF

    # Initialize dp for target sequence
    for i in range(1, m + 1):
        dp[i] = float('inf')

    current_start = 0  # start of the current "bessie" being tracked

    for i in range(n):
        c = s[i]
        # Update dp in reverse to prevent overwriting before checking
        for j in range(m, 0, -1):
            if