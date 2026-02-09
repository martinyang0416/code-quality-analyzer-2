import math

r, x, y, x_prime, y_prime = map(int, input().split())
dx = x_prime - x
dy = y_prime - y
distance_sq = dx ** 2 + dy ** 2

if distance_sq == 0:
    print(0)
else:
    distance = math.sqrt(distance_sq)
    steps = math.ceil(distance / (2 * r))
    print(steps)