import sys

def main():
    N = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    prefix = [0] * (N + 1)
    for i in range(N):
        prefix[i+1] = prefix[i] + a[i]

    for i in range(1, N+1):
        # Compute S_inc
        s_inc = []
        for L in range(1, i+1):
            for R in range(i, N+1):
                s = prefix[R] - prefix[L-1]
                s_inc.append(s)
        # Compute S_exc
        s_exc = []
        for L in range(1, N+1):
         