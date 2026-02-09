MOD = 10**9 + 7

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        current_parity = 0
        even = 1  # Initially, prefix sum 0 is even
        odd = 0
        res = 0
        for num in arr:
            current_parity = (current_parity + num) % 2
            if current_parity == 0:
                res += odd
                even += 1
            else:
                res += even
                odd += 1
            res %= MOD
        return res % MOD