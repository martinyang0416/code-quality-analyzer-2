import math

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    n = int(input[idx])
    idx += 1
    angles = []
    for _ in range(n):
        x = float(input[idx])
        y = float(input[idx + 1])
        idx += 2
        rad = math.atan2(y, x)
        deg = math.degrees(rad)
        if deg < 0:
            deg += 360.0
        angles.append(deg)
    
    angles.sort()
    max_gap = 0.0
    for i in range(n - 1):
        gap = angles[i + 1] - angles[i]
        if 