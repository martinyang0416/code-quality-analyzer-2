def find_dominant_tree(t, test_cases):
    results = []
    for case in test_cases:
        n, h = case
        if n == 1:
            results.append(1)
            continue
        
        left = [0] * n
        for i in range(1, n):
            if h[i-1] < h[i]:
                left[i] = left[i-1] + 1
            else:
                left[i] = 0
        
        right = [0] * n
        for i in range(n-2, -1, -1):
            if h[i] < h[i+1]:
                right[i] = right[i+1] + 1
      