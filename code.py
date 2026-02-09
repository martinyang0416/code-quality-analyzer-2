class TrieNode:
    __slots__ = ['children']
    def __init__(self):
        self.children = [None, None]  # children for 0 and 1

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    C = int(input[idx])
    idx += 1
    N = int(input[idx])
    idx += 1

    masks = []
    for _ in range(N):
        s = input[idx]
        idx += 1
        mask = 0
        for c in s:
            mask <<= 1
            if c == 'H':
                mask |= 1
        masks.append(mask)
  