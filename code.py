n, m = map(int, input().split())

factorial = 1
for i in range(1, m + 1):
    factorial *= i

if factorial % n == 0:
    print("YES")
else:
    print("NO")