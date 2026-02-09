n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

count_a = [0] * 6  # Using indices 1 to 5
count_b = [0] * 6

for num in a:
    count_a[num] += 1
for num in b:
    count_b[num] += 1

possible = True
for i in range(1, 6):
    if (count_a[i] + count_b[i]) % 2 != 0:
        possible = False
        break

if not possible:
    print(-1)
else:
    total_abs = 0
    for i in range(1, 6):
        total = count_a[i] + count_b[i]
        target = total // 2
      