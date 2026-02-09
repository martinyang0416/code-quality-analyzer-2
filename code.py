s = input().strip()
d1 = int(s[1])
d2 = int(s[2])
d3 = int(s[3])
d4 = int(s[4])
two_digit = d1 * 10 + d2
if d4 == 0:
    print(two_digit - d3)
else:
    print(two_digit)