def compute_h(x):
    res = 0
    while x > 0:
        res += x
        x = x // 2
    return res

def compute_j(x):
    if x == 1:
        return 1
    if x % 2 == 1:
        return x
    m = x
    k = 0
    while m % 2 == 0:
        m = m // 2
        k += 1
    return (m << k) + ((1 << k) - 1)

def calc(x):
    return compute_h(x) + compute_j(x)

def solve():
    import sys
    input = sys.stdin.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        P = int(input[idx]