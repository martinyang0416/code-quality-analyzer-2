import bisect

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0

    n = int(input[ptr])
    ptr += 1

    p = list(map(int, input[ptr:ptr + n]))
    ptr += n

    q = list(map(int, input[ptr:ptr + n]))
    ptr += n

    pos_p = [0] * (n + 1)
    for i in range(n):
        v = p[i]
        pos_p[v] = i + 1

    pos_q = [0] * (n + 1)
    for i in range(n):
        v = q[i]
        pos_q[v] = i + 1

    A = []
    for i in range(n):
        v = p[i]
        j = pos_q[v]
