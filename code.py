n = int(input())
nums = list(map(int, input().split()))
evens = []
odds = []
for num in nums:
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)
result = evens + odds
print(' '.join(map(str, result)))