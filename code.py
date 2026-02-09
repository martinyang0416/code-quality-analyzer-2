def isMatch(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    dp_prev = [False] * (n + 1)
    dp_prev[0] = True  # Empty pattern matches empty string

    # Initialize for the case when the string is empty
    for j in range(1, n + 1):
        if p[j - 1] == '*' and dp_prev[j - 1]:
            dp_prev[j] = True
        else:
            break  # Once a non '*' is found, subsequent cannot be matched

    # Iterate over each character in the string
    for i in range(1, m + 1):
        dp_cur