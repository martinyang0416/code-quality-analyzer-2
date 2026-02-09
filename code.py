s = input().strip()
total = sum(int(c) for c in s)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Yes" if is_prime(total) else "No")