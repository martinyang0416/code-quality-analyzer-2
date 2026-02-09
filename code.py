import sys
from collections import deque

def main():
    sys.setrecursionlimit(1 << 25)
    N = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    required = [False] * (N + 1)
    for i in range(N):
        if s[i] == '1':
            required[i+1] = True

    # Read the tree edges
    adj = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a, b = map(int, sys.stdin.readline().split())
        adj[a].append(b)
        adj[b].append(a)

    # Find base components using BF