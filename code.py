# Read the known characters and convert to a set for O(1) lookups
known = set(input().strip())

# Read the number of words
n = int(input())

# Process each word
for _ in range(n):
    word = input().strip()
    # Check if all characters in the word are in the known set
    can_read = all(char in known for char in word)
    print("Yes" if can_read else "No")