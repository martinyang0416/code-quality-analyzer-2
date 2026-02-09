import sys
from collections import deque

def main():
    n, m = map(int, sys.stdin.readline().split())
    dangerous = set()
    if m > 0:
        dangerous.update(map(int, sys.stdin.readline().split()))
    else:
        sys.stdin.readline()  # consume the line

    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * (n + 1)
    tot