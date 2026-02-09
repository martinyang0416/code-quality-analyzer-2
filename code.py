import sys
import bisect
import numpy as np

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))

    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + a[i]

    all_subarrays = []
    all_sums = []
    for start in range(n + 1):
        for end in range(start + 1, n + 1):
            s = prefix[end] - prefix[start]
            all_subarrays.append((start, end, s))
            all_sums.append(s)

    for i in range(n)