def maxDistance(position, m):
    position.sort()
    low = 1
    high = position[-1] - position[0]
    res = 0

    def can_place(d):
        count = 1
        prev = position[0]
        for pos in position[1:]:
            if pos - prev >= d:
                count += 1
                prev = pos
                if count == m:
                    return True
        return count >= m

    while low <= high:
        mid = (low + high) // 2
        if can_place(mid):
            res = mid
       