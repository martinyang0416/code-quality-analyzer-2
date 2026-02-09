import sys

class FenwickTree:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (self.n + 2)  # 1-based indexing

    def update(self, idx, delta):
        # idx is the value (1-based)
        while idx <= self.n:
            self.tree[idx] += delta
            idx += idx & -idx

    def query(self, idx):
        # Sum from 1 to idx (inclusive)
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= idx & -idx
        return res

d