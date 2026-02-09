MOD = 10**9 + 7

def maxSum(nums1, nums2):
    # Compute prefix sums for both arrays
    prefix1 = [0]
    for num in nums1:
        prefix1.append(prefix1[-1] + num)
    
    prefix2 = [0]
    for num in nums2:
        prefix2.append(prefix2[-1] + num)
    
    # Find common elements along with their indices in both arrays
    commons = []
    i = j = 0
    n1, n2 = len(nums1), len(nums2)
    while i < n1 and j < n2:
        a, b = nums1[i], nums2[j]
        if a == b:
            commons.appen