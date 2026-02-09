def isSubsequence(s: str, t: str) -> bool:
    ptr = 0
    len_t = len(t)
    for char in s:
        found = False
        while ptr < len_t:
            if t[ptr] == char:
                ptr += 1
                found = True
                break
            ptr += 1
        if not found:
            return False
    return True