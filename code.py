from collections import deque

def min_operations_to_bab(s):
    if s == "BAB":
        return 0
    visited = set()
    queue = deque()
    queue.append((s, 0))
    visited.add(s)
    
    while queue:
        current, steps = queue.popleft()
        
        # Generate all possible next states
        next_states = []
        
        # Replace first character if possible
        if len(current) >= 1:
            if current[0] == 'A':
                new_str = 'B' + current[1:]
            els