import sys
import math

def main():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    index = 1
    for _ in range(t):
        n = int(data[index])
        m = int(data[index + 1])
        index += 2
        
        a_odd = n - (n // 2)
        a_even = n // 2
        b_odd = m - (m // 2)
        b_even = m // 2
        
        numerator = a_odd * b_even + a_even * b_odd
        denominator = n * m
        
        if numerator == 0:
            print("0/1")
      