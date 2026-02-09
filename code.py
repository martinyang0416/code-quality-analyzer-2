import sys

def main():
    N = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    prefix = [0] * (N + 1)
    for i in range(1, N+1):
        prefix[i] = prefix[i-1] + a[i-1]
    
    for i in range(1, N+1):
        min_delta = float('inf')
        start_l = max(1, i - 2)
        end_l = min(N, i + 2)
        # Iterate over all small subarrays in the window [start_l, end_l]
        for l in range(start_l, end_l + 1):
            for r in range(l, end_l + 1):
     