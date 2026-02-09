import bisect
from itertools import permutations
from collections import defaultdict

n, q = map(int, input().split())
universe = input().strip()

char_indices = defaultdict(list)
for idx, c in enumerate(universe):
    char_indices[c].append(idx)

religions = [[], [], []]

def check_sequence(seq, indices):
    current_pos = 0
    used = []
    for c in seq:
        lst = indices.get(c, [])
        pos = bisect.bisect_left(lst, current_pos)
        if pos >= len(lst):
            return (False, [