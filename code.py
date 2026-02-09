def binary_search(array, target):
    lower = 0
    upper = len(array) - 1
    if upper == lower:
        return 0
    while lower < upper:   # use < instead of <=
        x = lower + (upper - lower) // 2
        val = array[x]
        if target == val:
            return x
        elif target > val:
            if lower == x:   # these two are the actual lines
                dist_left = target - array[lower]
                dist_right = array[upper] - target
                if dist_left == dis