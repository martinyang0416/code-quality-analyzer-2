def main():
    import sys
    input = sys.stdin.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        A = int(input[idx])
        B = int(input[idx+1])
        idx +=2
        
        len_A = len(bin(A)) - 2 if A !=0 else 1
        len_B = len(bin(B)) - 2 if B !=0 else 1
        n = max(len_A, len_B)
        
        a_bin = format(A, '0{}b'.format(n))
        b_bin = format(B, '0{}b'.format(n))
        
        max_xor = -1
        best_shift = 0
        
        for