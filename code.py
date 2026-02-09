import sys

def convert_seconds(sec):
    h = sec // 3600
    rem = sec % 3600
    m = rem // 60
    s = rem % 60
    return f"{h:02}:{m:02}:{s:02}"

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    T, H, S = map(int, line.split())
    if T == -1 and H == -1 and S == -1:
        break
    total_used = T * 3600 + H * 60 + S
    remaining = 7200 - total_used
    std_time = remaining
    triple_time = remaining * 3
    print(convert_seconds(std_time))
    print(c