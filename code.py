import sys

s = sys.stdin.read().strip()
words = s.split()
if not words:
    print('')
else:
    min_word = min(words, key=lambda x: len(x))
    result = [min_word]
    for word in words:
        result.append(word)
        result.append(min_word)
    print(' '.join(result))