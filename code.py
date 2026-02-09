import math

def main():
    import sys
    n = int(sys.stdin.readline())
    points = []
    for _ in range(n):
        x, y = map(float, sys.stdin.readline().split())
        points.append((x, y))
    
    max_dist = 0.0
    p1 = p2 = points[0]
    
    for i in range(n):
        for j in range(i+1, n):
            dx = points[i][0] - points[j][0]
            dy = points[i][1] - points[j][1]
            dist = dx*dx + dy*dy
            if dist > max_dist:
                max_dist = dist
      