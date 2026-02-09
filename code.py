import math
from typing import List

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            total += self.calculate_sum(num)
        return total
    
    def calculate_sum(self, n):
        if n == 1:
            return 0
        sum_div = 0
        count = 0
        sqrt_n = int(math.sqrt(n))
        for i in range(1, sqrt_n + 1):
            if n % i == 0:
                if i * i == n:
                    sum_div += i
   