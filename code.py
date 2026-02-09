import sys
from collections import defaultdict

def main():
    n = int(sys.stdin.readline())
    count_dict = defaultdict(int)
    for _ in range(n):
        s = sys.stdin.readline().strip()
        sorted_s = ''.join(sorted(s))
        count_dict[sorted_s] += 1
    total = 0
    for cnt in count_dict.values():
        if cnt >= 2:
            total += cnt * (cnt - 1) // 2
    print(total)

if __name__ == "__main__":
    main()