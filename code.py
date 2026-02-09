part_A = "What are you doing while sending "
part_B = "? Are you busy? Will you send "
f0 = "What are you doing at the end of the world? Are you busy? Will you save us?"

threshold = 60

def solve(n, k):
    current_n = n
    current_k = k
    while True:
        if current_n == 0:
            if current_k <= len(f0):
                return f0[current_k - 1]
            else:
                return '.'
        elif current_n >= threshold:
            if current_k <= 33:
                return pa