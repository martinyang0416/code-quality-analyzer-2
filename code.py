t = int(input())
for _ in range(t):
    s = input().strip()
    cnt0 = s.count('0')
    cnt1 = s.count('1')
    min_cnt = min(cnt0, cnt1)
    print("DA" if min_cnt % 2 == 1 else "NET")