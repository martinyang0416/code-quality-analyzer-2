def countNumbersWithUniqueDigits(n):
    if n == 0:
        return 1
    total = 10
    current = 9
    available = 9
    for k in range(2, min(n, 10) + 1):
        current *= available
        total += current
        available -= 1
    return total