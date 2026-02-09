MOD = 10**9 + 7

import sys

def main():
    input = sys.stdin.read
    data = input().split()
    T = int(data[0])
    index = 1
    for _ in range(T):
        N = int(data[index])
        K = int(data[index + 1])
        index += 2
        if N == 0:
            ans = ((K-1) * K) % MOD
        else:
            if K == 1:
                ans = (N * N) % MOD
            else:
                m = K // 2
                round_ = N + m
                if K % 2 == 0:
                    ans = ((rou