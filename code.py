def putaway(A, B, T, X, Y, W, S):
    if T == 0:
        return 0
    
    max_x = 0
    if A > 0:
        max_x = max(X)
    max_y = 0
    if B > 0:
        max_y = max(Y)
    
    C1 = 0  # can only be handled by weak
    C2 = 0  # can only be handled by small
    C3 = 0  # can be handled by both or either
    possible = True
    
    for i in range(T):
        is_weak = (W[i] < max_x)
        is_small = (S[i] < max_y)
        
        if not is_weak and not is_small:
            possible = Fa