import sys

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx+n]))
        idx += n
        c = list(map(int, data[idx:idx+n]))
        idx += n
        c_sorted = sorted(c)
        d = [a[i] - c_sorted[i] for i in range(n)]
        print(' '.join(map(str, d)))
        print(' '.join(map(str, d)))

if __name__ == '__main__':
   