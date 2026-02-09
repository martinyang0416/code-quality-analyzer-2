import sys
from collections import defaultdict, deque

def main():
    input = sys.stdin.read().split()
    idx = 0
    N, Q = int(input[idx]), int(input[idx+1])
    idx += 2

    adj = [[] for _ in range(N+1)]
    edges = []
    for _ in range(N-1):
        a = int(input[idx])
        b = int(input[idx+1])
        c = int(input[idx+2])
        d = int(input[idx+3])
        idx += 4
        edges.append((a, b, c, d))
        adj[a].append((b, c, d))
        adj[b].append((a, c, d))

    parent =