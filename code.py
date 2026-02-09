import bisect

def putaway(A, B, T, X, Y, W, S):
    can_weak = []
    can_small = []
    Wonly = 0
    Sonly = 0
    Both = 0
    eligible_weak = []
    eligible_small = []

    for i in range(T):
        w = W[i]
        s = S[i]
        cw = any(x > w for x in X)
        cs = any(y > s for y in Y)
        if not cw and not cs:
            return -1
        can_weak.append(cw)
        can_small.append(cs)
        if cw and not cs:
            Wonly += 1
        elif cs and not cw:
            