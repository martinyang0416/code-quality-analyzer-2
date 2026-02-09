MOD = 10**9 + 7

n = int(input())
c = list(map(int, input().split()))
d = list(map(int, input().split()))
q = int(input())
y_list = list(map(int, input().split()))

max_a1 = c[0] if n > 0 else 0
counts = [0] * (max_a1 + 1)

def compute_count(a1):
    if a1 < 0 or a1 > c[0]:
        return 0
    current = [0] * (c[0] + 1)
    current[a1] = 1
    for i in range(n-1):
        next_dp = [0] * (c[i+1] + 1)
        d_val = d[i]
        for a_prev in range(len(current)):
            if current[a_prev] 