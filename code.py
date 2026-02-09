from collections import deque

class Edge:
    __slots__ = ('to', 'rev', 'capacity')
    def __init__(self, to, rev, capacity):
        self.to = to
        self.rev = rev
        self.capacity = capacity

def max_flow(adj, s, t):
    N = len(adj)
    level = [0] * N
    ptr = [0] * N

    def bfs():
        q = deque()
        level[:] = [-1] * N
        level[s] = 0
        q.append(s)
        while q:
            v = q.popleft()
            for edge in adj[v]:
                if edge.capacity