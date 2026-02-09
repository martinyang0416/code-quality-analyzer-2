import sys

def main():
    n, x, y = map(int, sys.stdin.readline().split())
    for _ in range(n):
        a = int(sys.stdin.readline())
        low = 0.0
        high = a * max(1.0 / x, 1.0 / y) + 1.0
        for __ in range(100):
            mid = (low + high) / 2
            sum_mid = (mid * x).__floor__() + (mid * y).__floor__()
            if sum_mid < a:
                low = mid
            else:
                high = mid
        t = high
        sum_floor = (t * x).__floor__() + (t * y