def main():
    import sys
    input = sys.stdin.read().split()
    T = int(input[0])
    index = 1
    for _ in range(T):
        s = input[index]
        index += 1
        balance = 0
        count_balances = {0: 1}
        total = 0
        for c in s:
            if c == 'A':
                balance += 1
            else:
                balance -= 1
            # Get the current balance's count and add to total
            total += count_balances.get(balance, 0)
            # Update the co