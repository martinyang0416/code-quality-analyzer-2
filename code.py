import heapq

class Edge:
    def __init__(self, to, rev, capacity, cost):
        self.to = to
        self.rev = rev
        self.capacity = capacity
        self.cost = cost

def add_edge(adj, fr, to, capacity, cost):
    adj[fr].append(Edge(to, len(adj[to]), capacity, cost))
    adj[to].append(Edge(fr, len(adj[fr])-1, 0, -cost))

def min_cost_flow(adj, s, t, maxf):
    n = len(adj)
    res = 0.0
    h = [0.0] * n
    prevv = [0] * n
    preve = [0] * n
    INF = float('inf')

    flow = 0
  