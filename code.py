import sys

def main():
    input = sys.stdin.read().split()
    idx = 0
    n = int(input[idx]); idx +=1
    m = int(input[idx]); idx +=1
    r = int(input[idx]); idx +=1

    # Precompute distance matrices for each car using Floyd-Warshall
    dist = []
    for _ in range(m):
        d = []
        for i in range(n):
            row = list(map(int, input[idx:idx+n]))
            idx +=n
            d.append(row.copy())
        # Floyd-Warshall
        for k in range(n):
            for i in ra