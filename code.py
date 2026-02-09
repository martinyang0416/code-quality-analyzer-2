n, x = map(int, input().split())
a = list(map(int, input().split()))

roots = {}
depths = {}

for node in range(1, n+1):
    if node in roots:
        continue
    path = []
    current = node
    while True:
        if current in roots:
            root = roots[current]
            depth_current = depths[current]
            for nd in reversed(path):
                roots[nd] = root
                depth_current += 1
                depths[nd] = depth_current
            break
        predecess