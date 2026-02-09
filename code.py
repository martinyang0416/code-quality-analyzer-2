N, M = map(int, input().split())
bits = bin(N).count('1')
if bits <= M <= N and (M - bits) % 2 == 0:
    print("YES")
else:
    print("NO")