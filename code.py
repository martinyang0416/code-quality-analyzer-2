def determine_holder():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        N = int(input[idx])
        ID = int(input[idx + 1])
        idx += 2
        current = ID
        last_passer = None
        for _ in range(N):
            cmd = input[idx]
            if cmd == 'P':
                # Process P command
                new_id = int(input[idx + 1])
                idx += 2
                last_passer = current