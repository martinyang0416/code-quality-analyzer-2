import math

def compute_min_time(n, m, k, obstacles):
    g = math.gcd(n, m)
    d = 2 * g

    results = []
    for x, y in obstacles:
        a_options = [x, 2 * n - x]
        b_options = [y, 2 * m - y]

        possible_ts = []
        for a in a_options:
            for b in b_options:
                if (a - b) % d != 0:
                    continue

                N = 2 * n
                M = 2 * m
                C = (b - a) % M

                g_crt = math.gcd(N, M)
                