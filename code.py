from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    idx = 1
    group_seats = defaultdict(list)
    for _ in range(N):
        s = int(data[idx])
        g = int(data[idx+1])
        group_seats[g].append(s)
        idx += 2

    # Each group must have at least one seat, so no need to handle empty groups
    groups = list(group_seats.keys())
    if len(groups) == 0:
        print(0)
        return

    # P