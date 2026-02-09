import bisect

def putaway(A, B, T, X, Y, W, S):
    X_sorted = sorted(X) if A > 0 else []
    Y_sorted = sorted(Y) if B > 0 else []

    W_eligible = [False] * T
    S_eligible = [False] * T

    for i in range(T):
        wt = W[i]
        st = S[i]

        # Check eligibility for weak robots
        if A > 0:
            idx = bisect.bisect_right(X_sorted, wt)
            if idx < A:
                W_eligible[i] = True
        else:
            W_eligible[i] = False

        # Check eligibi