from collections import Counter

def deleteAndEarn(nums):
    if not nums:
        return 0
    counts = Counter(nums)
    sorted_nums = sorted(counts.keys())
    prev_prev_max = 0
    prev_max = 0
    prev_num = -1  # Initialize with a value that ensures the first num is not adjacent
    
    for num in sorted_nums:
        current_points = num * counts[num]
        if num == prev_num + 1:
            new_max = max(prev_max, prev_prev_max + current_points)
        else:
            new_max = pr