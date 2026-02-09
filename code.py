import sys
from collections import deque

MOD = 10**9 + 7

def main():
    input = sys.stdin.read().split()
    ptr = 0
    N = int(input[ptr])
    ptr += 1
    words = []
    for _ in range(N):
        words.append(input[ptr])
        ptr += 1
    t = input[ptr]
    ptr += 1

    # Build the trie
    nodes = [{'children': {}, 'failure': -1, 'output': [], 'combined_output': []}]

    for word in words:
        current = 0
        for c in word:
            if c not in nodes[current]['children']: