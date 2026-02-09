from collections import deque

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    N = int(input[idx])
    idx += 1
    M = int(input[idx])
    idx += 1

    adj = [[] for _ in range(N)]
    for _ in range(M):
        u = int(input[idx])
        idx += 1
        v = int(input[idx])
        idx += 1
        adj[u].append(v)
        adj[v].append(u)
    
    levels = [-1] * N
    levels[0] = 0
    q = deque([0])

    while q:
        u = q.popleft()
        for v in adj