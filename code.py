t, m = map(int, input().split())
allocated_blocks = []
next_id = 1

for _ in range(t):
    parts = input().split()
    if parts[0] == 'alloc':
        n = int(parts[1])
        gaps = []
        prev_end = -1
        for block in allocated_blocks:
            current_start = block['start']
            if current_start > prev_end + 1:
                gaps.append((prev_end + 1, current_start - 1))
            prev_end = block['start'] + block['size'] - 1
        if prev_end < m - 1:
            ga