def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr +=1
    for _ in range(T):
        N, M = int(input[ptr]), int(input[ptr+1])
        ptr +=2
        R = list(map(int, input[ptr:ptr+N]))
        ptr +=N
        monthly_ratings = []
        for i in range(N):
            C = list(map(int, input[ptr:ptr+M]))
            ptr +=M
            current = R[i]
            ratings = []
            for c in C:
                current += c
        