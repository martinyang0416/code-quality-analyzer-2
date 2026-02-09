n = int(input())
events = []
for _ in range(n):
    s, d = map(int, input().split())
    end = s + d
    events.append((s, 0))   # 0 represents start event
    events.append((end, 1)) # 1 represents end event

# Sort the events by time, and for same time, start events come before end events
events.sort(key=lambda x: (x[0], x[1]))

current = 0
max_current = 0

for time, typ in events:
    if typ == 0:
        current += 1
        if current > max_current:
            max_current = current
    els