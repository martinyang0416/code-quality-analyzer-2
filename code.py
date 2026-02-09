def can_separate(blue_x, red_x):
    max_blue = max(blue_x)
    min_red = min(red_x)
    
    if max_blue < min_red:
        return True
    else:
        max_red = max(red_x)
        min_blue = min(blue_x)
        if max_red < min_blue:
            return True
    return False

# Read input
import sys

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        parts = list(map(int, line.split()))
        if len(parts) == 0:
            c