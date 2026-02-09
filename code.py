import sys

def main():
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        N, M, L = map(int, line.strip().split())
        if N == 0 and M == 0 and L == 0:
            break
        data = list(map(float, sys.stdin.readline().strip().split()))
        
        # Precompute error for all intervals [start][end] (0-based, inclusive)
        error = [[0.0 for _ in range(N)] for _ in range(N)]
        for start in range(N):
            current_sub = []