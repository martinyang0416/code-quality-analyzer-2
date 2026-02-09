import sys
from collections import deque

class Dinic:
    def __init__(self, n):
        self.size = n
        self.graph = [[] for _ in range(n)]
        
    def add_edge(self, fr, to, cap):
        forward = [to, len(self.graph[to]), cap]
        backward = [fr, len(self.graph[fr]), 0]
        self.graph[fr].append(forward)
        self.graph[to].append(backward)
        
    def bfs_level(self, s, t, level):
        q = deque()
        level[:] = [-1] * self.size
        level[s] = 0
      