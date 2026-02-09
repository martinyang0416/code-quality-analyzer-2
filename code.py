n = int(input())
s = input().strip()
mod = 10**18 + 3
base = 911382629

prefix_hash = [0] * (n + 1)
power = [1] * (n + 1)
for i in range(n):
    prefix_hash[i+1] = (prefix_hash[i] * base + ord(s[i])) % mod
    power[i+1] = (power[i] * base) % mod

def get_hash(l, r):
    if l > r:
        return 0
    res = (prefix_hash[r+1] - prefix_hash[l] * power[r - l + 1]) % mod
    return res if res >= 0 else res + mod

result = []
max_k = (n + 1) // 2
for k in range(1, max_k + 1):
    i = k - 1
    j = n 