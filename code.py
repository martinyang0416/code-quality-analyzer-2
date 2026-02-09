MOD = 10**9 + 7

n, k = map(int, input().split())
a = list(map(int, input().split()))

if k == 0:
    print(' '.join(map(str, a)))
    exit()

max_fact = 2000
fact = [1] * (max_fact + 1)
for i in range(1, max_fact + 1):
    fact[i] = fact[i-1] * i % MOD

inv_fact = [1] * (max_fact + 1)
inv_fact[max_fact] = pow(fact[max_fact], MOD - 2, MOD)
for i in range(max_fact - 1, -1, -1):
    inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

comb = [0] * (2001)
for d in range(2001):
    if d == 0:
        comb[d] 