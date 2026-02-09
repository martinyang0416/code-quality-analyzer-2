import math

n = int(input())
for case in range(n):
    X, Y = map(int, input().split())
    log_x = math.log10(X)
    lower = math.log10(Y)
    upper = math.log10(Y + 1)
    lower_frac = lower - math.floor(lower)
    upper_frac = upper - math.floor(upper)
    E = 0
    while True:
        E += 1
        total = E * log_x
        f = total - math.floor(total)
        if lower_frac < upper_frac:
            if lower_frac <= f < upper_frac:
                break
        else:
            if f >= l