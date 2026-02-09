a, b, c = map(int, input().split())
t = ((a - b) * c + b - 1) // b
print(t)