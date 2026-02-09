import sys
from collections import defaultdict, deque

def main():
    n = int(sys.stdin.readline())
    strings = [sys.stdin.readline().strip() for _ in range(n)]
    unique_strings = list(set(strings))
    if len(unique_strings) != n:
        print("NO")
        return

    # Check if all are single character
    all_single = all(len(s) == 1 for s in unique_strings)
    if all_single:
        chars = [s[0] for s in unique_strings]
        if len(chars) != len(set(chars)):
            print("NO