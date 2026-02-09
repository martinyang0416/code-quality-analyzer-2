import bisect

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    for _ in range(t):
        n, m = int(data[idx]), int(data[idx+1])
        idx +=2
        a = list(map(int, data[idx:idx+n]))
        idx +=n
        b = list(map(int, data[idx:idx+n]))
        idx +=n
        
        type1 = []
        type2 = []
        for ai, bi in zip(a, b):
            if bi == 1:
                type1.append(ai)
            