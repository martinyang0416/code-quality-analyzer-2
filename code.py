import math

def mirrorReflection(p, q):
    if q == 0:
        return 0
    m = (p * q) // math.gcd(p, q)
    a, b = m // p, m // q
    if a % 2 == 0 and b % 2 == 1:
        return 0
    elif a % 2 == 1 and b % 2 == 1:
        return 1
    else:
        return 2