class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        MOD = 10**9 + 7
        A.sort()
        n = len(A)
        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i-1] * 2) % MOD
        
        sum_max = 0
        sum_min = 0
        for i in range(n):
            sum_max = (sum_max + A[i] * pow2[i]) % MOD
            sum_min = (sum_min + A[i] * pow2[n - 1 - i]) % MOD
        
        return (sum_max - sum_min) % MOD