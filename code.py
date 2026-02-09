a_part = "What are you doing while sending "  # Length 33
b_part = " Are you busy? Will you send "      # Length 29
f0 = "What are you doing at the end of the world? Are you busy? Will you save us?"  # Length 75

def solve():
    import sys
    q = int(sys.stdin.readline())
    for _ in range(q):
        n, k = map(int, sys.stdin.readline().split())
        current_level = n
        current_k = k
        while True:
            if current_level == 0:
                if current_k > 75:
          