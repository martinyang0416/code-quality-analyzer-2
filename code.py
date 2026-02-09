def putaway(A, B, T, X, Y, W, S):
    if T != 2:
        return -1  # According to problem constraints, T is 2
    
    robots = []
    if A == 2 and B == 0:
        robots = [('weak', X[0]), ('weak', X[1])]
    elif A == 1 and B == 1:
        robots = [('weak', X[0]), ('small', Y[0])]
    elif A == 0 and B == 2:
        robots = [('small', Y[0]), ('small', Y[1])]
    else:
        return -1  # Invalid case as per problem constraints
    
    allowed = []
    for toy in range(2):
        w = W[t