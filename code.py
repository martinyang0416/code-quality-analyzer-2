MOD = 998244353

n = int(input())
# The array is read but not used since the sum is n*(n+1)/2 regardless of the fixed values
input().split()

n_mod = n % MOD
sum_n = (n_mod * (n + 1)) % MOD
inv_two = pow(2, MOD-2, MOD)
result = (sum_n * inv_two) % MOD

print(result)