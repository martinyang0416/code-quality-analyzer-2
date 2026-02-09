s = input().strip()
total = sum(int(c) for c in s)
print("Yes" if total % 2 != 0 else "No")