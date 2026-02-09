import bisect

def putaway(A, B, T, X, Y, W, S):
    can_weak = [False] * T
    can_small = [False] * T
    for i in range(T):
        w = W[i]
        s = S[i]
        possible = any(x > w for x in X)
        can_weak[i] = possible
        possible_small = any(y > s for y in Y)
        can_small[i] = possible_small
        if not can_weak[i] and not can_small[i]:
            return -1

    M_list = []
    O_list = []
    P_list = []
    for i in range(T):
        cw = can_weak[i]
        cs = c