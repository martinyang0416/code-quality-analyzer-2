def minSwap(A, B):
    n = len(A)
    swap, noswap = 1, 0
    for i in range(1, n):
        new_swap = float('inf')
        new_noswap = float('inf')
        # Transition from previous not swapped
        if A[i] > A[i-1] and B[i] > B[i-1]:
            new_noswap = min(new_noswap, noswap)
        if B[i] > A[i-1] and A[i] > B[i-1]:
            new_swap = min(new_swap, noswap + 1)
        # Transition from previous swapped
        if A[i] > B[i-1] and B[i] > A[i-1]:
            new_noswap = min(n