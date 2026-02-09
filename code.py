n = int(input())
booked = []

for _ in range(n):
    s, d = map(int, input().split())
    preferred_start = s
    preferred_end = s + d - 1
    available = True
    for a, b in booked:
        if not (preferred_end < a or preferred_start > b):
            available = False
            break
    if available:
        new_interval = (preferred_start, preferred_end)
        inserted = False
        for j in range(len(booked)):
            if booked[j][0] > new_interval[0]:
                booked.in