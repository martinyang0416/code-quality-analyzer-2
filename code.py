import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        for _ in range(n-1):
            sys.stdin.readline()  # skip edges
        k1 = int(sys.stdin.readline())
        x_list = list(map(int, sys.stdin.readline().split()))
        k2 = int(sys.stdin.readline())
        y_list = list(map(int, sys.stdin.readline().split()))
        y_set = set(y_list)
        found = False
        
        # Check up to 3 nodes from my subtre