import sys
import math

MOD = 10**9 + 7

def main():
    N, M = map(int, sys.stdin.readline().split())
    ratings = []
    for _ in range(M):
        s = sys.stdin.readline().strip()
        ratings.append(s)
    
    # Create bitmask for each problem
    bitmask = []
    for i in range(N):
        bm = 0
        for j in range(M):
            if ratings[j][i] == 'H':
                bm |= 1 << j
        bitmask.append(bm)
    
    # Group by bitmask
    from collections import defaultdict
    