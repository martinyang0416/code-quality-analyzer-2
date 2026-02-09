s = input().strip()
a, b, c = map(int, s.split())

# Check for arithmetic sequence
diff1 = b - a
diff2 = c - b
if diff1 == diff2:
    print("Arithmetic Sequence")
else:
    # Check for geometric sequence
    if a == 0:
        # If a is 0, geometric is only possible if all terms are 0, which would have passed arithmetic check
        print("Neither")
    else:
        if b * b == a * c:
            print("Geometric Sequence")
        else:
            print("Neither")