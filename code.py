def minimal_max():
    import sys
    input = sys.stdin.read().split()
    
    n = int(input[0])
    sequence = list(map(int, input[1:n+1]))
    
    # Group into runs
    runs = []
    if not sequence:
        print(0)
        return
    current_x = sequence[0]
    current_m = 1
    for num in sequence[1:]:
        if num == current_x:
            current_m += 1
        else:
            runs.append((current_x, current_m))
            current_x = num
            current_m = 1
    runs.append((