n = int(input())
a = list(map(int, input().split()))
from collections import defaultdict

freq = defaultdict(int)

for num in a:
    msb = num.bit_length() - 1
    freq[msb] += 1

total = 0
for count in freq.values():
    if count >= 2:
        total += count * (count - 1) // 2

print(total)