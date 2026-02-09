n = int(input())
root = {}
count = 0
for _ in range(n):
    word = input().strip()
    current = root
    for c in word:
        if c not in current:
            current[c] = {}
            count += 1
        current = current[c]
print(count)