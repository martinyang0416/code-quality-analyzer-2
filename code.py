n, r, s = map(int, input().split())
books = list(map(int, input().split()))
books.sort()

count = 0

for b in books:
    if r < 0 or s < 0:
        continue
    initial_a = min(r, b // 3)
    rem = b - initial_a * 3
    if rem <= s:
        count += 1
        r -= initial_a
        s -= rem
    else:
        numerator = b - s + 2
        required_a_min = numerator // 3
        required_a_min = max(required_a_min, 0)
        available_a = min(r, b // 3)
        if available_a >= required_a_min:
 