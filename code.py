def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    while True:
        n = int(input[ptr])
        m = int(input[ptr+1])
        ptr += 2
        if n == 0 and m == 0:
            break
        vectors = []
        for _ in range(n):
            s = input[ptr]
            ptr += 1
            num = int(s, 2)
            vectors.append(num)
        # Compute S
        S = 0
        for num in vectors:
            S ^= num
        if S == 0:
            print(n)
      