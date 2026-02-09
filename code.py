def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

Y = int(input())
current = Y if Y % 2 == 1 else Y + 1

while True:
    if is_prime(current):
        print(current)
        break
    current += 2