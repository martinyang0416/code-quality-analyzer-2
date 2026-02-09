# Read the number of test cases
T = int(input())
for _ in range(T):
    # Read N and K for each test case
    N, K = map(int, input().split())
    # Read the list of numbers
    numbers = list(map(int, input().split()))
    # Compute the number of set bits for each number
    set_bits = [bin(num).count('1') for num in numbers]
    # Sort the set bits in descending order
    set_bits.sort(reverse=True)
    # Sum the top K values
    print(sum(set_bits[:K]))