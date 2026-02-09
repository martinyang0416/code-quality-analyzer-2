n = int(input())
a = list(map(int, input().split()))
m = int(input())

for _ in range(m):
    k, pos = map(int, input().split())
    # Create list of (-value, index) to sort by descending value and ascending index
    elements = [(-a[i], i) for i in range(n)]
    elements.sort()
    # Select first k elements and extract their indices
    selected_indices = [idx for (val, idx) in elements[:k]]
    # Sort the indices to maintain the original order
    selected_indices.sort()
    # Get the correspo