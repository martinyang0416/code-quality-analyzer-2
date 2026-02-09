a = int(input())
result = 1
for i in range(6):
    if a & (1 << i):
        result *= (i + 1)
print(result)