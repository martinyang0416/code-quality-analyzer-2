def smallestRangeII(A, K):
    A.sort()
    n = len(A)
    ans = A[-1] - A[0]
    for i in range(1, n):
        left_max = A[i-1] + K
        right_max = A[-1] - K
        current_max = max(left_max, right_max)
        left_min = A[0] + K
        right_min = A[i] - K
        current_min = min(left_min, right_min)
        current_diff = current_max - current_min
        if current_diff < ans:
            ans = current_diff
    return ans