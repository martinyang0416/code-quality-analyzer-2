def smallestDivisor(nums, threshold):
    low = 1
    high = max(nums)
    while low < high:
        mid = (low + high) // 2
        total = sum((num + mid - 1) // mid for num in nums)
        if total > threshold:
            low = mid + 1
        else:
            high = mid
    return low