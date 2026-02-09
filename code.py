import bisect

def main():
    import sys
    m, V = map(int, sys.stdin.readline().split())
    E = list(map(int, sys.stdin.readline().split()))
    max_efficiency = -1.0
    
    for p in range(m - 2):
        target = E[p] + V
        r = bisect.bisect_right(E, target) - 1
        
        if r >= p + 2:
            numerator = E[r] - E[p + 1]
            denominator = E[r] - E[p]
            
            if denominator == 0:
                continue
            
            efficiency = numer