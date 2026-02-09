def solve():
    import sys
    from collections import defaultdict

    t = sys.stdin.readline().strip()
    k = int(sys.stdin.readline())

    n = len(t)
    cnt = defaultdict(int)
    for c in t:
        cnt[c] += 1

    divisors = set()
    for d in range(1, int(k**0.5) + 1):
        if k % d == 0:
            if d <= n:
                divisors.add(d)
            if (k // d) <= n:
                divisors.add(k // d)
    divisors = sorted(divisors)

    required = defaultdict(list)
    for 