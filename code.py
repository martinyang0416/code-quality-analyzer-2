a = int(input())
print(1 if any(int(c) % 2 for c in str(a)) else 0)