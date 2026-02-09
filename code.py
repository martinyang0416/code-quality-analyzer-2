MOD = 10**9 + 7

def main():
    import sys
    from collections import deque

    N, M = map(int, sys.stdin.readline().split())
    strings = [sys.stdin.readline().strip() for _ in range(M)]
    
    # Build adjacency list for the DAG
    adj = [[] for _ in range(N)]
    in_degree = [0] * N

    for m in range(M):
        s = strings[m]
        for i in range(N):
            for j in range(N):
                if s[i] == 'H' and s[j] == 'E':
                    # Edge from j to i: j must come be