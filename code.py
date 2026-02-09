import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    
    xor_a = 0
    for num in a:
        xor_a ^= num
    
    xor_mod = 0
    for k in range(2, m + 1):
        q, r = divmod(n, k)
        sum_mod_k = q * (k - 1) * k // 2 + (r * (r + 1)) // 2
        xor_mod ^= sum_mod_k
    
    R = xor_a ^ xor_mod
    print(R)

if __name__ == "__main__":
    main()