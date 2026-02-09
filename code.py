import heapq
from collections import defaultdict

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]  # 1-based indexing for nodes

for _ in range(m):
    a, b, l, r = map(int, input().split())
    adj[a].append((b, l, r))
    adj[b].append((a, l, r))

heap = []
# Initialize with edges from node 1
for v, l, r in adj[1]:
    if l <= r:
        heapq.heappush(heap, (-(r - l + 1), l, r, v))

intervals = defaultdict(list)
found = False

while heap:
    neg_len, L, R, u = heapq.heappop