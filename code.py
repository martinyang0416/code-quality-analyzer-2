import bisect

def putaway(A, B, T, X, Y, W, S):
    # Sort the X and Y arrays to facilitate binary search
    X_sorted = sorted(X)
    Y_sorted = sorted(Y)
    
    only_weak = 0
    only_small = 0
    both = 0
    
    for i in range(T):
        w = W[i]
        s = S[i]
        
        # Determine can_weak
        can_weak = False
        if A > 0:
            idx = bisect.bisect_right(X_sorted, w)
            if idx < len(X_sorted):
                can_weak = True
        else:
            