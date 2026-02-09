import sys

def main():
    sys.setrecursionlimit(1 << 25)
    C, N = map(int, sys.stdin.readline().split())
    masks = []
    for _ in range(N):
        s = sys.stdin.readline().strip()
        mask = 0
        for i in range(C):
            bit = 1 if s[i] == 'H' else 0
            mask |= bit << (C - 1 - i)
        masks.append(mask)
    
    from collections import defaultdict
    count = defaultdict(int)
    for m in masks:
        count[m] += 1

    class Node:
        __slots__ = ['child