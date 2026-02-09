k, n = map(int, input().split())
stones = [tuple(map(int, input().split())) for _ in range(k)]
monsters = [tuple(map(int, input().split())) for _ in range(n)]

count = 0

for m in monsters:
    mx, my = m
    afraid = False
    for t in stones:
        tx, ty = t
        dx = mx - tx
        dy = my - ty
        distance_sq_m = dx ** 2 + dy ** 2
        blocked = False
        for m_prime in monsters:
            if m_prime == m:
                continue
            mpx, mpy = m_prime
          