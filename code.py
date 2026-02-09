def findKthBit(n: int, k: int) -> str:
    def helper(n: int, k: int) -> int:
        if n == 1:
            return 0
        L = (1 << (n - 1)) - 1
        if k == L + 1:
            return 1
        elif k <= L:
            return helper(n - 1, k)
        else:
            j = k - (L + 1)
            original_pos = L - j + 1
            return 1 - helper(n - 1, original_pos)
    
    return str(helper(n, k))