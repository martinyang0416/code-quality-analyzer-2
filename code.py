n, k = map(int, input().split())
d = list(map(int, input().split()))

if d.count(0) != 1:
    print(-1)
    exit()

max_d = max(d)

layers = {}
for i in range(n):
    node = i + 1
    dist = d[i]
    if dist not in layers:
        layers[dist] = []
    layers[dist].append(node)

# Check if all layers from 0 to max_d-1 are present when needed
for current_d in range(max_d):
    if current_d not in layers or len(layers[current_d]) == 0:
        if (current_d + 1) in layers and len(layers[current_d 