a = int(input())
if a < 10:
    print("YES")
else:
    tens = a // 10
    units = a % 10
    if tens + units == 10:
        print("YES")
    else:
        print("NO")