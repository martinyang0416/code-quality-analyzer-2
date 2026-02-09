MOD = 10**9 + 7

def main():
    import sys
    input = sys.stdin.read().split()
    T = int(input[0])
    test_cases = list(map(int, input[1:T+1]))
    if not test_cases:
        return
    max_Ti = max(test_cases)
    
    # Precompute a and b arrays
    max_a = max_Ti
    a = [0] * (max_a + 1)
    if max_a >= 0:
        a[0] = 1
    if max_a >= 1:
        a[1] = 0
    if max_a >= 2:
        a[2] = (a[1] + a[0] + 1) % MOD
    for ti in range(3, max_a + 1):
        a[ti] = (a[ti-1] + a[ti-2] + 