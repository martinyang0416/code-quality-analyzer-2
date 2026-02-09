def are_equivalent(a, b):
    if a == b:
        return True
    n = len(a)
    if n % 2 != 0:
        return False
    if sorted(a) != sorted(b):
        return False
    mid = n // 2
    a1, a2 = a[:mid], a[mid:]
    b1, b2 = b[:mid], b[mid:]
    return (are_equivalent(a1, b1) and are_equivalent(a2, b2)) or (are_equivalent(a1, b2) and are_equivalent(a2, b1))

s1 = input().strip()
s2 = input().strip()

print("YES" if are_equivalent(s1, s2) else "NO")