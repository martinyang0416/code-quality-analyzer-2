def generate_string(A, B):
    result = []
    while A > 0 or B > 0:
        if len(result) >= 2 and result[-1] == result[-2]:
            last_char = result[-1]
            if last_char == 'a':
                if B == 0:
                    result.append('a')
                    A -= 1
                else:
                    result.append('b')
                    B -= 1
            else:
                if A == 0:
                    result.append('b')
                    B -= 1
             