import itertools

def is_square(p1, p2, p3, p4):
    points = [p1, p2, p3, p4]
    dist_sq = []
    for (x1, y1), (x2, y2) in itertools.combinations(points, 2):
        dx = x1 - x2
        dy = y1 - y2
        dist_sq.append(dx * dx + dy * dy)
    if len(dist_sq) != 6:
        return False
    unique = sorted(list(set(dist_sq)))
    if len(unique) != 2:
        return False
    a, b = unique
    if a == 0:
        return False
    if b != 2 * a:
        return False
    return dist_sq.count(a) 