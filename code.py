n, m = map(int, input().split())
statements = []
count_plus = [0] * (n + 1)
count_minus = [0] * (n + 1)

for _ in range(n):
    stmt = input().strip()
    t = stmt[0]
    a = int(stmt[1:])
    statements.append((t, a))
    if t == '+':
        count_plus[a] += 1
    else:
        count_minus[a] += 1

total_minus = sum(count_minus)
possible_leaders = set()

for x in range(1, n + 1):
    cp = count_plus[x]
    cm = count_minus[x]
    c = cp + (total_minus - cm)
    if c == m:
        possible_lead