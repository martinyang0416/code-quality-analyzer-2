def maxNonOverlapping(nums, target):
    prefix_map = {0: -1}
    current_sum = 0
    count = 0
    last_end = -1
    for j in range(len(nums)):
        current_sum += nums[j]
        if (current_sum - target) in prefix_map:
            start = prefix_map[current_sum - target] + 1
            if start > last_end:
                count += 1
                last_end = j
                # Reset the prefix_map to track sums after j
                prefix_map = {current_sum: j}
                contin