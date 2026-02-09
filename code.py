import sys
from sys import stdin

def main():
    sys.setrecursionlimit(1 << 25)
    n = int(stdin.readline())
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    parent = [0] * (n + 1)
    parent[1] = -1  # Root has no parent
    size = [1] * (n + 1)
    T = 0
    stack = [(1, False)]
    
    while stack:
        node, visited = stack.pop()
        if not visited:
          