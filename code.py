n, m = map(int, input().split())
s = list(input())
for _ in range(m):
    p, c = input().split()
    p = int(p) - 1  # Convert to 0-based index
    s[p] = c
modified = ''.join(s)
vowels = {'a', 'e', 'i', 'o', 'u'}
for v in vowels:
    if v not in modified:
        print(-1)
        exit()
print(modified)