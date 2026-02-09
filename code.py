import sys
import bisect

def main():
    sys.setrecursionlimit(1 << 25)
    N, Q = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()
    spec = sys.stdin.readline().strip()

    L_indices = []
    R_indices = []
    for idx, c in enumerate(s):
        if c == 'L':
            L_indices.append(idx)
        else:
            R_indices.append(idx)

    # Compute ℓ and r arrays
    ell = [(L_indices[i] + 1) for i in range(N)]
    r = [(R_indices[i] + 1) for i in range(N)]
