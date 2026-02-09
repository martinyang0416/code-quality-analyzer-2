T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    forgotten_words = input().split()
    modern_set = set()
    for _ in range(K):
        parts = input().split()
        modern_set.update(parts[1:])
    result = ['YES' if word in modern_set else 'NO' for word in forgotten_words]
    print(' '.join(result))