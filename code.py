import math
import sys

def main():
    n, c, d = map(int, sys.stdin.readline().split())
    points = []
    for _ in range(n):
        r, w = map(int, sys.stdin.readline().split())
        a = r - c
        b = w - d
        points.append((a, b))
    
    # Compute angles and handle edge cases
    thetas = []
    for a, b in points:
        if a == 0 and b == 0:
            continue  # But problem states |ri'| + |wi'| >0, so this cannot happen
        theta = math.atan2(b, a)
        thetas.app