import bisect

def compute_min_M(robots, toys_list, N):
    low = 1
    high = N
    best = high
    while low <= high:
        mid = (low + high) // 2
        if canAssign(mid, robots, toys_list, N):
            best = mid
            high = mid - 1
        else:
            low = mid + 1
    return best

def canAssign(M, robots, toys_list, N):
    ptr = 0
    for x in robots:
        idx = bisect.bisect_left(toys_list, x, ptr, N)
        available = idx - ptr
        take = min(available, M)
 