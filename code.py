def main():
    import sys
    input = sys.stdin.read().split()
    N = int(input[0])
    idx = 1
    result = []

    for _ in range(N):
        a = int(input[idx])
        b = int(input[idx+1])
        c = int(input[idx+2])
        d = int(input[idx+3])
        e = int(input[idx+4])
        idx +=5

        # Convert a, b, c each to 2-bit binary
        def num_to_2bit(n):
            return format(n, '02b')

        first_part = num_to_2bit(a) + num_to_2bit(b) + num_to_2bit(c)
        second_