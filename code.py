from collections import defaultdict

n = int(input())
count_map = defaultdict(int)
result = 0

for _ in range(n):
    s = input().strip()
    reversed_s = s[::-1]
    result += count_map[reversed_s]
    count_map[s] += 1

print(result)