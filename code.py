import sys

def main():
    N, K, T = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    # Compute deltas for each position
    deltas = []
    for j in range(K):
        next_j = (j + 1) % K
        delta = (A[next_j] - A[j]) % N
        deltas.append(delta)
    
    # For each residue r mod N, compute the displacement_contribution[r]
    displacement_contribution = [0] * N
    for j in range(K):
        c_j = A[j] % N  # c_j = A_j mod N
        delt