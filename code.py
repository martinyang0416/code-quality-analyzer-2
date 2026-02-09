import sys

def main():
    sys.setrecursionlimit(1 << 25)
    N, Q = map(int, sys.stdin.readline().split())
    S = sys.stdin.readline().strip()
    special = sys.stdin.readline().strip()
    queries = [tuple(map(int, sys.stdin.readline().split())) for _ in range(Q)]

    # Parse L and R positions correctly
    L = []
    R = []
    for i in range(2 * N):
        if S[i] == 'L':
            L.append(i + 1)
        else:
            R.append(i + 1)
    L = L[:N]
    R = R[:N]

    # Precompute p