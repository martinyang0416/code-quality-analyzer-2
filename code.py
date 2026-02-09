import bisect

def putaway(A, B, T, X, Y, W, S):
    sorted_X = sorted(X)
    sorted_Y = sorted(Y)
    
    W_only = 0
    S_only = 0
    Both = 0
    
    for i in range(T):
        w = W[i]
        s = S[i]
        # Check eligibility for weak robots
        idx_weak = bisect.bisect_right(sorted_X, w)
        is_weak = (idx_weak < len(sorted_X))
        # Check eligibility for small robots
        idx_small = bisect.bisect_right(sorted_Y, s)
        is_small = (idx_small < len(sorted_Y))
     