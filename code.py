import numpy as np

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    N = int(input[idx]); idx +=1
    K = int(input[idx]); idx +=1
    T = int(input[idx]); idx +=1
    A = list(map(int, input[idx:idx+K]))
    idx += K

    # Compute contrib array
    contrib = [0] * N
    for r in range(N):
        if r == 0:
            contrib[r] = T // N
        else:
            contrib[r] = (T - r + N) // N

    # Compute B_j for each j in A
    B = [(1 - a) % N for a in A]

 