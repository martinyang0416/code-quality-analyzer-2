import sys
from collections import deque

def main():
    sys.setrecursionlimit(1 << 25)
    N = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    edges = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a, b = map(int, sys.stdin.readline().split())
        edges[a].append(b)
        edges[b].append(a)

    # Collect Cowflix nodes
    cow_nodes = []
    for i in range(1, N+1):
        if s[i-1] == '1':
            cow_nodes.append(i)
    M = len(cow_nodes)
    if M == 0