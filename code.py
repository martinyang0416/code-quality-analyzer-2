n, m = map(int, input().split())
c = list(map(int, input().split()))

cnt = [0] * m
for num in c:
    rem = num % m
    cnt[rem] += 1

total_pairs = 0

# Handle remainder 0
total_pairs += cnt[0] // 2

# Iterate through possible remainders
for r in range(1, (m // 2) + 1):
    if r != m - r:
        total_pairs += min(cnt[r], cnt[m - r])
    else:
        # Handle the case where r is exactly half of m (even m)
        total_pairs += (cnt[r] // 2)

print(total_pairs * 2)