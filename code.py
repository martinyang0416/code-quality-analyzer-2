def is_valid_square(points):
    dists = []
    for i in range(4):
        for j in range(i + 1, 4):
            dx = points[i][0] - points[j][0]
            dy = points[i][1] - points[j][1]
            dists.append(dx * dx + dy * dy)
    unique = sorted(set(dists))
    if len(unique) != 2:
        return False
    a, b = unique
    if b != 2 * a or a == 0:
        return False
    count_a = dists.count(a)
    count_b = dists.count(b)
    return count_a == 4 and count_b == 2

n = int(input())
fo