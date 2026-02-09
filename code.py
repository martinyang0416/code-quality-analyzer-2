n, k = map(int, input().split())
s = list(map(int, input().split()))

prefix = [0] * (n + 1)
for i in range(n):
    prefix[i + 1] = prefix[i] + s[i]

max_avg = 0.0

for L in range(k, n + 1):
    for i in range(n - L + 1):
        total = prefix[i + L] - prefix[i]
        avg = total / L
        if avg > max_avg:
            max_avg = avg

print("{0:.15f}".format(max_avg))