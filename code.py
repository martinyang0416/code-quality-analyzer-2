n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_sorted = sorted(a)
b_sorted = sorted(b)

min_x = m  # Initialize with the maximum possible value

for j in range(n):
    # Calculate the candidate x based on the j-th element of sorted b and the first element of sorted a
    x_candidate = (b_sorted[j] - a_sorted[0]) % m
    # Generate the transformed array after adding x_candidate and mod m
    transformed = [(num + x_candidate) % m for nu