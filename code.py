def canMeasureWater(x, y, z):
    if z == 0:
        return True
    if x + y < z:
        return False
    from math import gcd
    g = gcd(x, y)
    return z % g == 0