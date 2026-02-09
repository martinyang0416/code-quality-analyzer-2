def compute_white(a, b, c, d):
    total = (c - a + 1) * (d - b + 1)
    start_white = (a + b) % 2 == 0
    return (total + start_white) // 2

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    
    initial_white = (n * m + 1) // 2
    area_white = (x2 - x1 + 1) * (y2 - y1 + 1)
    area_black = (x4 - x3 + 1) * (y4 - y3 + 1)
    
    x_start = max(x1, x3)
    x_end = min(x2, x4)