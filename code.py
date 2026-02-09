import math
from functools import reduce

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    gcd_all = reduce(math.gcd, a)
    print(gcd_all * n)