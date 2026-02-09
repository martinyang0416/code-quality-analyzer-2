import sys

def main():
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        line = line.strip()
        while line == '':
            line = sys.stdin.readline().strip()
        N, M = map(int, line.split())
        if N == 0 and M == 0:
            break
        C = []
        for _ in range(M):
            c = int(sys.stdin.readline().strip())
            C.append(c)
        xs = []
        for _ in range(N):
            x = int(sys.stdin.readline