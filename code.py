from collections import deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    n = int(sys.stdin.readline())
    adj = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    parent = [-1] * (n + 1)
    visited = [False] * (n + 1)
    
    q = deque()
    q.append(1)
    visited[1] = True
    parent[1] = -1  # root has no parent
    
    while q:
        u = q.popleft()
  