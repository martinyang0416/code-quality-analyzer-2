n, *rest = map(int, open(0).read().split())
a = rest[:n]

from collections import defaultdict

freq = defaultdict(int)
for num in a:
    freq[num] += 1

unique = list(freq.keys())
len_unique = len(unique)

if len_unique >= 3:
    print(3)
elif len_unique == 2:
    a1, a2 = unique[0], unique[1]
    if freq[a1] >= 2 and freq[a2] >= 2:
        print(4)
    else:
        print(-1)
else:
    print(-1)