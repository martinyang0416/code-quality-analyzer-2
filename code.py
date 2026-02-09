def putaway(A, B, T, X, Y, W, S):
    max_X = -float('inf')
    if A > 0:
        max_X = max(X)
    max_Y = -float('inf')
    if B > 0:
        max_Y = max(Y)

    W_only = 0
    S_only = 0
    Both = 0

    for i in range(T):
        w = W[i]
        s = S[i]
        weak_ok = (w < max_X)
        small_ok = (s < max_Y)
        if weak_ok and small_ok:
            Both += 1
        elif weak_ok:
            W_only += 1
        elif small_ok:
            S_only += 1
        else:
            ret