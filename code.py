from collections import deque

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr += 1
    for _ in range(T):
        N, K = int(input[ptr]), int(input[ptr+1])
        ptr += 2
        c = list(map(int, input[ptr:ptr+N]))
        ptr += N
        
        # Build the graph
        graph = [[] for _ in range(N+1)]  # 1-based indexing for left nodes
        for i in range(1, N+1):
            for j in range(i+1, N+1):
                if abs(