n = int(input())

def generate_patterns(n):
    patterns = []
    def backtrack(current, max_num):
        if len(current) == n:
            patterns.append(current.copy())
            return
        for next_num in range(max_num + 2):
            backtrack(current + [next_num], max(max_num, next_num))
    if n == 0:
        return []
    backtrack([0], 0)
    return patterns

patterns = generate_patterns(n)
strings = [''.join(chr(ord('a') + num) for num in p) for p in patterns]
strings.sort()

