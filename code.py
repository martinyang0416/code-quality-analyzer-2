import math

x = int(input())

if x == 1:
    print(1, 1)
else:
    def factorize(n):
        factors = {}
        while n % 2 == 0:
            factors[2] = factors.get(2, 0) + 1
            n = n // 2
        i = 3
        while i * i <= n:
            while n % i == 0:
                factors[i] = factors.get(i, 0) + 1
                n = n // i
            i += 2
        if n > 1:
            factors[n] = 1
        return factors

    factors = factorize(x)
    
    divisors = [1]
    for p 