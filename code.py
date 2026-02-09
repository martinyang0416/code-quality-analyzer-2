s = input().strip()
last_digit = s[-1]
print(0 if int(last_digit) % 2 == 0 else 1)