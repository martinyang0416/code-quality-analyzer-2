import sys

def longest_common_substring(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    n = len(s1)
    m = len(s2)
    max_length = 0
    prev_row = [0] * (m + 1)
    for i in range(n):
        current_row = [0] * (m + 1)
        for j in range(m):
            if s1[i] == s2[j]:
                current_row[j+1] = prev_row[j] + 1
                if current_row[j+1] > max_length:
                    max_length = current_row[j+1]
            else:
                current_row[j+1] = 0
       