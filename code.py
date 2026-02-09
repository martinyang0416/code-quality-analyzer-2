n = int(input())
s = input().strip()
count_8 = s.count('8')
max_phones = n // 11
print(min(count_8, max_phones))