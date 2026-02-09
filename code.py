def min_good(fronts, backs):
    candidates = sorted(set(fronts + backs))
    for x in candidates:
        conflict = False
        for f, b in zip(fronts, backs):
            if f == x and b == x:
                conflict = True
                break
        if conflict:
            continue
        for f, b in zip(fronts, backs):
            if (b == x and f != x) or (f == x and b != x):
                return x
    return 0