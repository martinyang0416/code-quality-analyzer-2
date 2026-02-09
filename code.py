def main():
    import sys
    input = sys.stdin.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        N = int(input[idx])
        k = int(input[idx+1])
        idx +=2
        x = k +1
        count =0
        while x % 2 ==0:
            count +=1
            x = x //2
        print("ON" if count >= N else "OFF")

if __name__ == "__main__":
    main()