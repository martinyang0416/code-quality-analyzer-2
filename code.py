n, L = map(int, input().split())
intervals = [tuple(map(int, input().split())) for _ in range(n)]

# Compute x
sorted_intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))
current_end = 0
count = 0
i = 0
possible = True

while current_end < L:
    max_r = current_end
    while i < len(sorted_intervals) and sorted_intervals[i][0] <= current_end:
        if sorted_intervals[i][1] > max_r:
            max_r = sorted_intervals[i][1]
        i += 1
    if max_r == current_end:
        possible =