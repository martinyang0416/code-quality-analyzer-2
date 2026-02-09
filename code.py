import sys

def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        p, q = map(int, sys.stdin.readline().split())
        d = list(map(int, sys.stdin.readline().split()))
        if q < len(d):
            print(d[q])
            continue
        # Compute digits up to q
        while len(d) <= q:
            current_len = len(d)
            s = 0
            for i in range(1, p+1):
                idx = current_len - i
                sign = (-1) ** (i + 1)
                