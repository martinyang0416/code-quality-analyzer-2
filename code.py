def findTheLongestSubstring(s: str) -> int:
    vowel_map = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
    first_occurrence = {0: -1}
    mask = 0
    max_len = 0
    for i, char in enumerate(s):
        if char in vowel_map:
            mask ^= 1 << vowel_map[char]
        if mask in first_occurrence:
            current_len = i - first_occurrence[mask]
            if current_len > max_len:
                max_len = current_len
        else:
            first_occurrence[mask] = i
    return max_l