import heapq

n = int(input())
animals = []
for _ in range(n):
    f, d = map(int, input().split())
    animals.append((d, f))

animals.sort()
heap = []
sum_total = 0

for d, f in animals:
    heapq.heappush(heap, f)
    sum_total += f
    if len(heap) > d:
        removed = heapq.heappop(heap)
        sum_total -= removed

print(sum_total)