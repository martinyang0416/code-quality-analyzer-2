class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        
        negative = (dividend < 0) ^ (divisor < 0)
        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)
        quotient = 0
        
        while abs_dividend >= abs_divisor:
            temp = abs_divi