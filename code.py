import sys
from collections import deque

def main():
    s = sys.stdin.read().strip()
    target = 'bessie'
    n = len(s)
    pos = [deque() for _ in range(6)]
    total = 0
    for j, c in enumerate(s):
        for i in range(5, -1, -1):
            if c == target[i]:
                if i == 0:
                    pos[0].append(j)
                else:
                    if pos[i-1]:
                        prev_pos = pos[i-1].popleft()
                        pos[i].append(prev_pos)
       