import math

n = int(input())
for _ in range(n):
    a_str, b_str = input().split()
    a = int(a_str)
    if a == 0:
        if all(c == '0' for c in b_str):
            print(0)
        else:
            print(int(b_str))
    else:
        mod = 0
        for c in b_str:
            mod = (mod * 10 + int(c)) % a
        print(math.gcd(a, mod))