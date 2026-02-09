# Read the input values
A, B, C = map(int, input().split())

# Check if the sum of A and B is at least C
if A + B >= C:
    print("Yes")
else:
    print("No")