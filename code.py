def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    N = int(input[idx])
    idx += 1
    M = int(input[idx])
    idx += 1

    D = []
    for _ in range(N):
        D.append(int(input[idx]))
        idx += 1

    W = []
    for _ in range(M):
        W.append(int(input[idx]))
        idx += 1

    INF = float('inf')
    dp = [ [INF] * (M + 1) for _ in range(N + 1) ]
    dp[0][0] = 0

    for i in range(1, N + 1):
        d = D[i - 1]
        current_min = INF
        