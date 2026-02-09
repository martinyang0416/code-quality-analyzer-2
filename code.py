import sys
from collections import deque

def main():
    sys.setrecursionlimit(1 << 25)
    n, k = map(int, sys.stdin.readline().split())
    parents = list(map(int, sys.stdin.readline().split()))
    children = [[] for _ in range(n+1)]  # 1-based
    for i in range(2, n+1):
        p = parents[i-2]
        children[p].append(i)
    
    # Compute depths using BFS
    depth = [0] * (n + 1)
    q = deque()
    q.append(1)
    while q:
        u = q.popleft()
        for v in children[u]:
       