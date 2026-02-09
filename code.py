import heapq

def maxPerformance(n, speed, efficiency, k):
    engineers = sorted(zip(efficiency, speed), key=lambda x: -x[0])
    sum_speed = 0
    heap = []
    max_perf = 0
    MOD = 10**9 + 7
    
    for eff, spd in engineers:
        current = spd + sum_speed
        current_perf = current * eff
        if current_perf > max_perf:
            max_perf = current_perf
        heapq.heappush(heap, spd)
        sum_speed += spd
        if len(heap) > k - 1:
            removed = heapq.heappop(