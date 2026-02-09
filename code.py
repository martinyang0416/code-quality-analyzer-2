import sys

MAX_VALUE_STR = '1000000000000'

def is_valid_part(s_part):
    if len(s_part) == 0:
        return False
    if len(s_part) > 13:
        return False
    if len(s_part) > 1 and s_part[0] == '0':
        return False
    if len(s_part) == 13:
        return s_part == MAX_VALUE_STR
    return True

def part_to_num(s_part):
    if len(s_part) == 13:
        return 10**12
    return int(s_part)

def process_string(s):
    L = len(s)
    if L < 4:
        return "unlucky"
    max_sum = 