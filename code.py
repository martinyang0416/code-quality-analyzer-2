def main():
    import sys
    t = sys.stdin.read().strip()
    n = len(t)
    if n == 0:
        print(0)
        return

    # Precompute prefix sums for b, e, s, i
    pre_b = [0] * (n + 1)
    pre_e = [0] * (n + 1)
    pre_s = [0] * (n + 1)
    pre_i = [0] * (n + 1)

    for i in range(n):
        pre_b[i+1] = pre_b[i]
        pre_e[i+1] = pre_e[i]
        pre_s[i+1] = pre_s[i]
        pre_i[i+1] = pre_i[i]
        c = t[i]
        if c == 'b':
            pre_b[i+1] += 1
        elif c == '