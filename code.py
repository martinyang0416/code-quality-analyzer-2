import sys

class TrieNode:
    __slots__ = ['children']
    def __init__(self):
        self.children = [None, None]

def main():
    C, N = map(int, sys.stdin.readline().split())
    masks = []
    for _ in range(N):
        s = sys.stdin.readline().strip()
        mask = 0
        for c in s:
            mask = (mask << 1) | (1 if c == 'H' else 0)
        masks.append(mask)
    
    # Build the trie
    root = TrieNode()
    for mask in masks:
        current = root
        for bit_pos in rev