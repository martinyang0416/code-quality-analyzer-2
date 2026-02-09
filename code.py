import heapq

def compute_g(s):
    mod = 10**9 + 7
    b = 100001
    l = len(s)
    res = 0
    for i in range(l):
        char_val = ord(s[i])
        exponent = l - (i + 1)
        power = pow(b, exponent, mod)
        term = (char_val * power) % mod
        res = (res + term) % mod
    return res

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    n = int(data[idx])
    idx += 1
    q = int(data[idx])
    idx += 1
    s = data[idx]
    idx += 1
