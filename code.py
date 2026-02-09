n = int(input())
health = list(map(int, input().split()))
P = int(input())

health_sorted = sorted(health)
sum_initial = 0
m = 0
for h in health_sorted:
    if sum_initial + h > P:
        break
    sum_initial += h
    m += 1
remaining_energy = P - sum_initial
remaining_candidates = health_sorted[m:]
max_total = 0

max_k = min(m, len(remaining_candidates))
for k in range(0, max_k + 1):
    if k > len(remaining_candidates):
        continue
    sum_action2 = sum(remaining_candidates[-k:]) if k >