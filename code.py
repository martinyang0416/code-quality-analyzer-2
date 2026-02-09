from collections import defaultdict

def subarraysDivByK(A, K):
    count_map = defaultdict(int)
    count_map[0] = 1
    prefix_mod = 0
    result = 0
    for num in A:
        prefix_mod = (prefix_mod + num) % K
        result += count_map[prefix_mod]
        count_map[prefix_mod] += 1
    return result