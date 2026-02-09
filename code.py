def maxVowels(s: str, k: int) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    current = 0
    for i in range(k):
        if s[i] in vowels:
            current += 1
    max_count = current
    for i in range(k, len(s)):
        outgoing = s[i - k]
        if outgoing in vowels:
            current -= 1
        incoming = s[i]
        if incoming in vowels:
            current += 1
        if current > max_count:
            max_count = current
    return max_count