def main():
    import sys
    input = sys.stdin.read().split()
    T = int(input[0])
    for i in range(1, T+1):
        S = input[i]
        reversed_S = S[::-1]
        count = 0
        for a, b in zip(S, reversed_S):
            if a != b:
                count += 1
        print(count // 2)

if __name__ == "__main__":
    main()