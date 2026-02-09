import sys

for line in sys.stdin:
    a = list(map(int, line.strip().split()))
    b_line = sys.stdin.readline()
    if not b_line:
        break
    b = list(map(int, b_line.strip().split()))
    
    hits = sum(1 for i in range(4) if a[i] == b[i])
    common = len(set(a) & set(b))
    blow = common - hits
    print(hits, blow)