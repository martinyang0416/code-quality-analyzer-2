def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        N, M = int(input[idx]), int(input[idx+1])
        idx +=2
        A = list(map(int, input[idx:idx+M]))
        idx += M
        count_ones = A.count(1)
        required = M - 1 - count_ones
        print(max(required, 0))

if __name__ == "__main__":
    main()