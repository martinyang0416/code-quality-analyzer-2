p = int(input())
vowels = {'a', 'e', 'i', 'o', 'u'}
for _ in range(p):
    s1 = input().strip()
    s2 = input().strip()
    s1_vowels = set(c for c in s1 if c in vowels)
    s2_vowels = set(c for c in s2 if c in vowels)
    if s1_vowels & s2_vowels:
        print("YES")
    else:
        print("NO")