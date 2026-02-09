def can_split(p, n):
    groups = [ [], [], [] ]
    last = [ -1, -1, -1 ]
    count = [0, 0, 0]
    for idx, num in enumerate(p):
        assigned = False
        # Try to assign to the group with the smallest last position that is less than current index
        # Also, don't exceed the count n for any group
        for i in range(3):
            if count[i] < n and last[i] < idx:
                # Check if this group is available and can take this index
                # We prefer the group w