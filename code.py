from collections import defaultdict, Counter
from typing import List

def count_pairs(arr: List[int], T: int) -> int:
    freq = defaultdict(int)
    count = 0
    for num in arr:
        if T % num == 0:
            quotient = T // num
            count += freq.get(quotient, 0)
        freq[num] += 1
    return count

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        # Compute frequency maps for squares of elements in both arrays
        freq1 = Count