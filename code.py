def minDays(bloomDay, m, k):
    if m * k > len(bloomDay):
        return -1
    
    left, right = min(bloomDay), max(bloomDay)
    ans = -1
    
    while left <= right:
        mid = (left + right) // 2
        current = 0
        bouquets = 0
        
        for day in bloomDay:
            if day <= mid:
                current += 1
                if current == k:
                    bouquets += 1
                    current = 0
            else:
                current = 0
        
     