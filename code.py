import sys

def main():
    input = sys.stdin.read().split()
    idx = 0
    t = int(input[idx])
    idx += 1
    for _ in range(t):
        n = int(input[idx])
        idx += 1
        a = list(map(int, input[idx:idx+n]))
        idx += n
        
        fixed_max = 0
        for i in range(n-1):
            if a[i] != -1 and a[i+1] != -1:
                current = abs(a[i] - a[i+1])
                if current > fixed_max:
                    fixed_max = current
        
        edges = []
   