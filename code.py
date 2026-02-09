a = int(input())
e = a.bit_length() - 1
if (2 ** e) == a:
    print(e)
else:
    print(e + 1)