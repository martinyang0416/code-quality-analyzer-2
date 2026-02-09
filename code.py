import sys

def to_bits(n):
    return bin(n)[2:].zfill(2)

def main():
    lines = sys.stdin.read().splitlines()
    N = int(lines[0])
    result = []
    for line in lines[1:N+1]:
        a, b, c, d, e = map(int, line.split())
        bits = []
        # Convert first three numbers to 2 bits each
        for num in [a, b, c]:
            bits.append(to_bits(num))
        # Convert last two numbers to 2 bits each
        for num in [d, e]:
            bits.append(to_bits(num))
        combined 