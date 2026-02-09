import sys

def main():
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        N = int(input[idx])
        idx +=1
        A = list(map(int, input[idx:idx+N]))
        idx += N
        sum_A = sum(A)
        if sum_A >= 0:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()