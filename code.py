n, *rest = map(int, open(0).read().split())
p = rest[:n]

count = 0
i = 0
while i < n:
    if p[i] == i + 1:
        if i + 1 < n and p[i+1] == i + 2:
            count += 1
            i += 2
        else:
            count += 1
            i += 1
    else:
        i += 1
print(count)