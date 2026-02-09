s, v1, v2, t1, t2 = map(int, input().split())
time1 = 2 * t1 + s * v1
time2 = 2 * t2 + s * v2
if time1 < time2:
    print("First")
elif time2 < time1:
    print("Second")
else:
    print("Friendship")