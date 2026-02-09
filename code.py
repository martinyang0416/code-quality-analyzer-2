import sys
from collections import deque

def main():
    p = float(sys.stdin.readline())
    N = int(sys.stdin.readline())
    edges = [[] for _ in range(N +1)]
    for _ in range(N-1):
        x,y,c = map(int, sys.stdin.readline().split())
        edges[x].append((y, c))
        edges[y].append((x, c))
    
    parent = [0]*(N+1)
    cost_to_parent = [0]*(N+1)
    visited = [False]*(N+1)
    q = deque([1])
    visited[1] =True
    parent[1]=0
    
    while q:
        u = q.popleft()
        f