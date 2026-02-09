def main():
    import sys
    N = int(sys.stdin.readline())
    temperatures = list(map(int, sys.stdin.readline().split()))
    D = int(sys.stdin.readline())
    
    temperatures.sort()
    max_len = 0
    left = 0
    for right in range(N):
        while temperatures[right] - temperatures[left] > D:
            left += 1
        current_len = right - left + 1
        if current_len > max_len:
            max_len = current_len
    print(N - max_len)

if __name__ == "__main__":
    main()