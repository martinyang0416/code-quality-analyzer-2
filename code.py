s = input().strip()
digits = list(map(int, s[1:]))
total = sum(digits)
fourth_digit = digits[3]
if fourth_digit == 0:
    total += 10
else:
    total += 1
print(total)