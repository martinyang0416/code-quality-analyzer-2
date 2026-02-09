import sys

def main():
    C, N = map(int, sys.stdin.readline().split())
    all_ones = (1 << C) - 1
    masks = []
    mask_set = set()

    for _ in range(N):
        s = sys.stdin.readline().strip()
        mask = 0
        for c in s:
            mask <<= 1
            if c == 'H':
                mask |= 1
        masks.append(mask)
        mask_set.add(mask)
    
    # Precompute the popcount for all masks in the set
    # Not needed here, but might help
    # Precompute all possible cand