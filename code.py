def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    M = int(input[idx])
    idx += 1
    L = int(input[idx])
    idx += 1
    
    intervals = []
    for _ in range(L):
        p = int(input[idx])
        idx +=1
        q = int(input[idx])
        idx +=1
        if p > q:
            p, q = q, p
        intervals.append((p, q-1))
    
    if not intervals:
        print(1)
        return
    
    intervals.sort(key=lambda x: x[1])
    
    splits = []
    current_en