import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

min_a = min(a)
max_a = max(a)

def compute_weakness(x):
    if n == 0:
        return 0.0
    # Compute max subarray sum
    current_max = a[0] - x
    max_sum = current_max
    for num in a[1:]:
        current_max = max(num - x, current_max + (num - x))
        max_sum = max(max_sum, current_max)
    # Compute min subarray sum
    current_min = a[0] - x
    min_sum = current_min
    for num in a[1:]:
  