from heapq import heappush, heappop

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    q = int(data[idx])
    idx += 1

    types = list(map(int, data[idx:idx + n]))
    idx += n

    unique_types = list(sorted(set(types)))
    type_to_idx = {t: i for i, t in enumerate(unique_types)}
    T = len(unique_types)

    adj = [[] for _ in range(n + 1)]  # 1-based
    for _ in range(m)