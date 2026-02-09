H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]
h, w = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(h)]

max_sum = None

for i in range(H - h + 1):
    for j in range(W - w + 1):
        match = True
        for di in range(h):
            if not match:
                break
            for dj in range(w):
                if B[i + di][j + dj] != C[di][dj]:
           