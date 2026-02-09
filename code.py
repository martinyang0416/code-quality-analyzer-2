import sys
import math

MOD = 10**9 + 7

def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        B = list(map(int, sys.stdin.readline().split()))
        P = sum(B)
        g = math.gcd(P, 5)
        exponent = 5 // g
        n = pow(2, exponent, MOD)
        result = pow(n, P, MOD)
        print(result)

if __name__ == "__main__":
    main()