def longestDiverseString(a: int, b: int, c: int) -> str:
    res = []
    counts = {'a': a, 'b': b, 'c': c}
    
    while True:
        # Check if all counts are zero
        total = counts['a'] + counts['b'] + counts['c']
        if total == 0:
            break
        
        # Determine the last two characters in the result
        last_char = res[-1] if res else ''
        second_last_char = res[-2] if len(res) >= 2 else ''
        
        # Determine forbidden character if last two are 