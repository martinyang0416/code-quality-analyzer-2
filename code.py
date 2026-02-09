def f(bs):
    return int(bs, 2) // (1 << n - 1) * a[-1] + sum(a[i] for i in range(min(n - 1, len(bs))) if bs[-i - 1] == '1')
n, x = map(int, input().split())
*a, = map(int, input().split())
for i in range(1, n):
    a[i] = min(a[i], 2 * a[i - 1])
bx = '0' * n + bin(x)[2:]
ans = f(bx)
for i in range(len(bx)):
    if bx[i] == '0':
        ans = min(ans, f(bx[:i] + '1' + '0' * (len(bx) - i - 1)))
print(ans)