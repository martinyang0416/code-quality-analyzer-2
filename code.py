# Read the number of test cases
T = int(input())
for _ in range(T):
    N = int(input().split()[0])  # Read N from each test case
    print((N // 2) + 1)