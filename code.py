n = int(input())
x = list(sorted(map(int, input().split())))


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

tgcd = x.pop(0)
for i in x:
    tgcd = gcd(tgcd, i)

print(tgcd * n)
