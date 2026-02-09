n = int(input())
s = input().strip()
red = s.count('R')
blue = len(s) - red
print("Yes" if red > blue else "No")