import sys

def generate_partitions():
    elements = [1, 2, 3, 4, 5, 6]
    all_partitions = []
    
    def backtrack(remaining, path):
        if not remaining:
            all_partitions.append(path.copy())
            return
        first = remaining[0]
        for i in range(1, len(remaining)):
            pair = (first, remaining[i])
            new_remaining = remaining[1:i] + remaining[i+1:]
            path.append(pair)
            backtrack(new_remaining, path)
            path.pop()
