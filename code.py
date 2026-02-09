n, k = map(int, input().split())
nums = list(map(int, input().split()))

# The first element is m, which is part of the allowed moves, so the starting player always wins
if k % 2 == 1:
    print("Alice")
else:
    print("Bob")