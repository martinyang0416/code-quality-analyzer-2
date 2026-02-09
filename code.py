import sys

def main():
    while True:
        n, m = map(int, sys.stdin.readline().split())
        if n == 0 and m == 0:
            break
        degree = [0] * n
        for _ in range(m):
            x, y, c = map(int, sys.stdin.readline().split())
            degree[x] += c
            degree[y] += c
        min_cut = min(degree)
        print(min_cut)

if __name__ == "__main__":
    main()