import collections

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)
        if k > n:
            return False
        counts = collections.Counter(s)
        odds = sum(1 for v in counts.values() if v % 2 != 0)
        min_k = max(1, odds) if odds else 1
        return k >= min_k