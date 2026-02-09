import sys

def main():
    n, t = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    
    # Precompute log_table for finding the maximum exponent k where 2^k <= length
    log_table = [0] * (n + 1)
    for i in range(2, n + 1):
        log_table[i] = log_table[i // 2] + 1
    max_k = log_table[n]
    
    # Initialize the Sparse Table
    st = [[0] * n for _ in range(max_k + 1)]
    for i in range(n):
        st[0][i] = arr[i]
    
    # Fill the S