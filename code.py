import bisect

s = input().strip()
q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(q)]

even_values = list(range(2, 27, 2))  # 2, 4, ..., 26

from collections import defaultdict
positions = defaultdict(list)
for idx, c in enumerate(s, 1):  # 1-based index
    value = ord(c) - 96
    if value % 2 == 0:
        positions[value].append(idx)

for x, y in queries:
    count = 0
    for v in even_values:
        lst = positions.get(v, [])
        if not lst:
            con