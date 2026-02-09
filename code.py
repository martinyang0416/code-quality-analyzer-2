# Read the list of integers from the first input line
numbers = list(map(int, input().split()))

# Read the index and the new value from the second input line
i, x = map(int, input().split())

# Update the list at the specified index
numbers[i] = x

# Print the modified list
print(numbers)