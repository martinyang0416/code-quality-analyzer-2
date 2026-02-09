def putaway(A, B, T, X, Y, W, S):
    # Check if each toy can be handled by at least one robot
    for i in range(T):
        possible = False
        # Check weak robots
        if A > 0:
            for x in X:
                if W[i] < x:
                    possible = True
                    break
        # Check small robots if not possible yet
        if not possible and B > 0:
            for y in Y:
                if S[i] < y:
                    possible = True
                    bre