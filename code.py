def maxUniqueSplit(s: str) -> int:
    max_count = 0
    n = len(s)
    
    def backtrack(start, used):
        nonlocal max_count
        if start == n:
            current = len(used)
            if current > max_count:
                max_count = current
            return
        for end in range(start + 1, n + 1):
            substr = s[start:end]
            if substr not in used:
                used.add(substr)
                backtrack(end, used)
                used.remove(substr)
   