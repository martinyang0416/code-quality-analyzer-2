import sys

def solve():
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        N, D = int(input[idx]), int(input[idx + 1])
        idx += 2
        C = list(map(int, input[idx:idx + N]))
        idx += N
        C.sort()
        
        low = 0.0
        high = 1e18
        eps = 1e-12  # Increased precision for binary search
        
        # Perform binary search with sufficient iterations
        for _ in range(100):
           