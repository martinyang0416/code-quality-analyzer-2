n = int(input())
arr = list(map(int, input().split()))

if n < 2:
    print(-1)
else:
    max_right = arr[-1]
    max_product = -1
    best_a = None
    best_b = None

    for i in range(n-2, -1, -1):
        current = arr[i]
        if current < max_right:
            product = current * max_right
            if product > max_product:
                max_product = product
                best_a = current
                best_b = max_right
        # Update max_right for next iteration
        ma