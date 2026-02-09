import bisect

def putaway(A, B, T, X, Y, W, S):
    if A == 0 and B == 0:
        return -1  # According to problem constraints, this shouldn't happen
    
    # Sort the X and Y arrays
    sorted_X = sorted(X) if A != 0 else []
    sorted_Y = sorted(Y) if B != 0 else []
    
    count_w_only = 0
    count_s_only = 0
    flex = 0
    
    for i in range(T):
        w = W[i]
        s = S[i]
        
        # Determine can_w
        if A == 0:
            can_w = False
        else:
           