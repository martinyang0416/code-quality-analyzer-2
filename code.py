m = int(input())
if m > 0:
    for i in range(m):
        row = []
        for j in range(m):
            d1 = i
            d2 = (m - 1) - i
            d3 = j
            d4 = (m - 1) - j
            min_d = min(d1, d2, d3, d4)
            row.append(str(min_d))
        print(' '.join(row))