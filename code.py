def maxSubarraySumCircular(A):
    # Compute maximum subarray sum using Kadane's algorithm
    max_current = max_so_far = A[0]
    for num in A[1:]:
        max_current = max(num, max_current + num)
        max_so_far = max(max_so_far, max_current)
    
    # If all elements are negative, return the maximum element (handled by max_so_far)
    if max_so_far < 0:
        return max_so_far
    
    # Compute minimum subarray sum using Kadane's algorithm for min
    min_current = min_so_far = A[0]
 