def find132pattern(nums):
    n = len(nums)
    if n < 3:
        return False
    
    min_so_far = [0] * n
    min_so_far[0] = nums[0]
    current_min = nums[0]
    
    for j in range(1, n):
        min_so_far[j] = current_min
        if nums[j] < current_min:
            current_min = nums[j]
    
    stack = []
    for j in range(n-1, -1, -1):
        if nums[j] > min_so_far[j]:
            while stack and stack[-1] <= min_so_far[j]:
                stack.pop()
            if stack and stac