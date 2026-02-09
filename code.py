import sys

def main():
    sys.setrecursionlimit(1 << 25)
    N = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    prefix = [0] * (N + 1)
    for i in range(N):
        prefix[i + 1] = prefix[i] + a[i]

    for i in range(N):
        # Compute S_in_sums: subarrays including i (0-based)
        S_in = [prefix[r + 1] - prefix[l] for l in range(i + 1) for r in range(i, N)]
        
        # Compute S_out_sums: subarrays not including i
        part1 = []  # subar