from collections import deque

n = int(input())
b = input().strip()
buildings = list(b)
queue = deque()

# Initialize queue with all initial 'D's
for i in range(n):
    if buildings[i] == 'D':
        queue.append(i)

# Process each 'D' to destroy adjacent 'S's
while queue:
    i = queue.popleft()
    for dx in (-1, 1):
        ni = i + dx
        if 0 <= ni < n and buildings[ni] == 'S':
            buildings[ni] = 'D'
            queue.append(ni)

# Count the remaining 'S's
count = sum(1 for c 