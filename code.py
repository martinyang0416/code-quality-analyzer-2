def get_divisors():
    divisors = []
    for i in range(1, 361):
        if 360 % i == 0:
            divisors.append(i)
    divisors.sort(reverse=True)
    return divisors

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    divisors = get_divisors()
    for _ in range(T):
        n = int(input[idx])
        idx += 1
        a = list(map(int, input[idx:idx+n]))
        idx += n
        found = False
        for d in divisors:
   