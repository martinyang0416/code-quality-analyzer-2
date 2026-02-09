MOD = 10**9 + 7

def main():
    import sys
    input = sys.stdin.read().split()
    N = int(input[0])
    V = list(map(int, input[1:N+1]))
    
    # Precompute factorials modulo MOD
    fact = [1] * (N + 2)
    for i in range(1, N + 2):
        fact[i] = fact[i-1] * i % MOD
    
    # Precompute inverse of 1..N modulo MOD
    inv = [0] * (N + 2)
    inv[1] = 1
    for i in range(2, N + 2):
        inv[i] = MOD - MOD // i * inv[MOD % i] % MOD
    
    # Precompute harmonic numbers H[0..N+1]
   