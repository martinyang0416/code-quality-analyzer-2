import sys

def main():
    input = sys.stdin.read
    data = input().split()
    T = int(data[0])
    idx = 1
    for _ in range(T):
        N = int(data[idx])
        S = int(data[idx+1])
        idx += 2
        if N == 1:
            print(S)
        else:
            if S < 2 or S > 9 * N:
                print(-1)
            else:
                if N >= 3:
                    print(0)
                else:
                    print(S - 1)
                    
if __name__ == "__main__":
 