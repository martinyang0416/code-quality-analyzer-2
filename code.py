import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    ptr = 0
    T = data[ptr]
    ptr += 1
    for _ in range(T):
        N = data[ptr]
        Q = data[ptr + 1]
        ptr += 2
        a = data[ptr:ptr + N]
        ptr += N
        # Compute prefix sums
        prefix = [0] * (N + 1)
        for i in range(1, N + 1):
            prefix[i] = prefix[i - 1] + a[i - 1]
        # Process queries
        for __ in range(Q):
            X = data[ptr]
            Y = data[p