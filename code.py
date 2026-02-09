from collections import deque

def canReach(arr, start):
    if arr[start] == 0:
        return True
    n = len(arr)
    visited = [False] * n
    queue = deque([start])
    visited[start] = True
    
    while queue:
        current = queue.popleft()
        jump = arr[current]
        for delta in (jump, -jump):
            next_idx = current + delta
            if 0 <= next_idx < n and not visited[next_idx]:
                if arr[next_idx] == 0:
                    return True
             