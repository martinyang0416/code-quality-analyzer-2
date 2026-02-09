a, b, c = map(int, input().split())
total = a + b + c
if total % 2 != 0:
    print("No")
else:
    half = total // 2
    if (a == half or b == half or c == half) or (a + b == half) or (a + c == half) or (b + c == half):
        print("Yes")
    else:
        print("No")