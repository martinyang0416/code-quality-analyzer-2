def main():
    import sys
    input = sys.stdin.read().splitlines()
    n, r, c = map(int, input[0].split())
    words = input[1].split()
    if not words:
        print()
        return

    # Precompute prefix sums and s array
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + len(words[i])
    s = [prefix_sum[i] + i for i in range(n + 1)]

    # Compute next_line_start
    next_line_start = [0] * n
    for l in range(n):
        target = s[l] + 