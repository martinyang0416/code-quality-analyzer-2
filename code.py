def shortestSuperstring(A):
    n = len(A)
    # Compute overlap[i][j] = maximum suffix of A[i] matching prefix of A[j]
    overlap = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                max_ov = 0
                for k in range(min(len(A[i]), len(A[j])), 0, -1):
                    if A[i].endswith(A[j][:k]):
                        max_ov = k
                        break
                overlap[i][j] = max_ov

    # DP[mask][i] =