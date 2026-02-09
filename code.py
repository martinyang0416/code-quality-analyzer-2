from collections import deque
from collections import defaultdict

def numOfMinutes(n, headID, manager, informTime):
    adj = defaultdict(list)
    for i in range(n):
        if manager[i] != -1:
            adj[manager[i]].append(i)
    
    max_time = 0
    time_informed = [0] * n
    q = deque([headID])
    
    while q:
        current = q.popleft()
        for sub in adj.get(current, []):
            time_informed[sub] = time_informed[current] + informTime[current]
            if time_info