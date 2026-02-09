import sys

for line in sys.stdin:
    line = line.strip()
    if line == '0':
        break
    n = int(line)
    totals = {}
    order = []
    for _ in range(n):
        parts = sys.stdin.readline().strip().split()
        i, p, q = parts[0], int(parts[1]), int(parts[2])
        amount = p * q
        if i not in totals:
            totals[i] = 0
            order.append(i)
        totals[i] += amount
    result = [emp_id for emp_id in order if totals[emp_id] >= 1000000]
    if not result:
  