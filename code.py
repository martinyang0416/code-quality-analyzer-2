def main():
    row1 = {'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'}
    row2 = {'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'}
    row3 = {'Z', 'X', 'C', 'V', 'B', 'N', 'M'}

    s = input().strip()

    # Check all characters are in row1
    if all(c in row1 for c in s):
        print("YES")
        return
    # Check all characters are in row2
    if all(c in row2 for c in s):
        print("YES")
        return
    # Check all characters are in row3
    if all(c in row3 for c in s):
     