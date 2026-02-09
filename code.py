import sys

def main():
    input = sys.stdin.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        n = int(input[idx])
        k = int(input[idx+1])
        idx +=2
        if k == 2 or n == k or k == 4:
            print(-1)
        else:
            m = k -2
            if n % m != 0:
                print(-1)
            else:
                block = '('*(m//2) + ')'*(m//2)
                print(block * (n//m))

if __name__ == "__main__":
    main()