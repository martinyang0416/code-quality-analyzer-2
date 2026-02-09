MOD = 998244353

def compute_f(n):
    if n == 0:
        return []
    prev_dp = [[0] * (n + 2) for _ in range(2)]
    prev_dp[0][1] = 1  # first element is 0, zeros=1
    for i in range(1, n):
        curr_dp = [[0] * (n + 2) for _ in range(2)]
        for last_bit in [0, 1]:
            for zeros in range(i + 1):  # zeros up to previous step (i elements)
                if prev_dp[last_bit][zeros] == 0:
                    continue
                for flip in [0, 1]:
                    new_l