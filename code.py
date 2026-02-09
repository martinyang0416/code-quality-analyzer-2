import bisect

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    N = int(input[ptr])
    ptr += 1
    Q = int(input[ptr])
    ptr += 1

    s = input[ptr]
    ptr += 1
    spec_str = input[ptr]
    ptr += 1

    # Parse left and right endpoints
    lefts = []
    rights = []
    for i in range(len(s)):
        c = s[i]
        if len(lefts) < N and c == 'L':
            lefts.append(i + 1)  # positions are 1-based
        elif len(rights) < N and c == 'R':
         