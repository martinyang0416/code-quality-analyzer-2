import bisect

def putaway(A, B, T, X, Y, W, S):
    X_sorted = sorted(X)
    Y_sorted = sorted(Y)
    
    a = 0  # toys can only go to weak
    b = 0  # can only go to small
    c = 0  # can go to either
    
    for i in range(T):
        wi = W[i]
        si = S[i]
        
        # Check possible_w: is there any X[j] > wi?
        possible_w = bisect.bisect_right(X_sorted, wi) < len(X_sorted)
        
        # Check possible_s: is there any Y[j] > si?
        possible_s = bisect.bisect_ri