n, k, M = map(int, input().split())
t_list = list(map(int, input().split()))
sorted_t = sorted(t_list)
sum_t = sum(sorted_t)
max_x = min(n, M // sum_t) if sum_t != 0 else 0
max_points = 0

for x in range(max_x + 1):
    time_used = x * sum_t
    if time_used > M:
        continue
    remaining = M - time_used
    points = x * (k + 1)
    for tj in sorted_t:
        possible = n - x
        if possible <= 0:
            continue
        cost_per = tj
        max_possible = possible
        total_