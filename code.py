n = int(input())
a = list(map(int, input().split()))
t = list(map(int, input().split()))

categories = sorted(zip(t, a), key=lambda x: (-x[0], x[1]))
parent = {}

def find(x):
    if x not in parent:
        return x
    root = x
    while root in parent:
        root = parent[root]
    current = x
    while current in parent and parent[current] != root:
        next_node = parent[current]
        parent[current] = root
        current = next_node
    return root

total = 0
for ti, ai in categor