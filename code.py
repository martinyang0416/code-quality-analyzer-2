import sys
from collections import defaultdict

def main():
    sys.setrecursionlimit(1 << 25)
    n = int(sys.stdin.readline())
    edges = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, sys.stdin.readline().split())
        edges[u].append(v)
        edges[v].append(u)
    f = list(map(int, sys.stdin.readline().split()))
    f = [0] + f  # 1-based indexing

    parent = [0] * (n + 1)
    size = [0] * (n + 1)
    count = [0] * (n + 1)
    mono = [False] * (n + 1)
