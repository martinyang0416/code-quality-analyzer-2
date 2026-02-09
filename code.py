n = int(input())
a = list(map(int, input().split()))
prefix = [0]
for num in a:
    prefix.append(prefix[-1] + num)
result = []
for k in range(1, n + 1):
    sum_first = prefix[k]
    sum_last = prefix[n] - prefix[n - k]
    if sum_first == sum_last:
        result.append(str(k))
print(' '.join(result))