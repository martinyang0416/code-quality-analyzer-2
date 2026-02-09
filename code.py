from collections import deque
from defaultdict import defaultdict

def minJumps(arr):
    n = len(arr)
    if n == 1:
        return 0
    
    # Create a dictionary to map each value to its indices
    value_indices = defaultdict(list)
    for i, num in enumerate(arr):
        value_indices[num].append(i)
    
    visited = [False] * n
    queue = deque([(0, 0)])
    visited[0] = True
    
    while queue:
        current_idx, steps = queue.popleft()
        # Check if we've reached the last in