t = int(input())
for _ in range(t):
    all_durations = []
    total_n = 0
    for _ in range(7):
        parts = list(map(int, input().split()))
        ni = parts[0]
        total_n += ni
        starts_ends = parts[1:]
        for i in range(ni):
            start = starts_ends[2*i]
            end = starts_ends[2*i +1]
            duration = end - start
            all_durations.append(duration)
    all_durations.sort()
    required = (3 * total_n + 3) // 4
    sum_attended = sum(all_duratio