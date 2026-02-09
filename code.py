import sys

def main():
    input = sys.stdin.read
    data = input().split()
    ptr = 0
    t = int(data[ptr])
    ptr += 1
    for _ in range(t):
        n, q = int(data[ptr]), int(data[ptr+1])
        ptr += 2
        s = data[ptr]
        ptr += 1
        prefix_sum = [0] * (n + 1)
        for i in range(1, n+1):
            prefix_sum[i] = prefix_sum[i-1] + (1 if s[i-1] == '1' else 0)
        for __ in range(q):
            l = int(data[ptr])
            r = int(data[ptr+1])
            pt