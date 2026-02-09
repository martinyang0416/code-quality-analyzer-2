import math

n, p = map(int, input().split())

t = (p // 2) + 1

s = 0.0
for k in range(t, p + 1):
    s += math.comb(p, k) * (0.5 ** p)

prob = 1.0 - (1.0 - s) ** n

# Format the output to 8 decimal places
print("{0:.8f}".format(prob))