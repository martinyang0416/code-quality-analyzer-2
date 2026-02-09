import sys

def is_sharp(A, B, C):
    ab_x = B[0] - A[0]
    ab_y = B[1] - A[1]
    bc_x = C[0] - B[0]
    bc_y = C[1] - B[1]
    dot = ab_x * bc_x + ab_y * bc_y
    if dot <= 0:
        return True
    ab_sq = ab_x ** 2 + ab_y ** 2
    bc_sq = bc_x ** 2 + bc_y ** 2
    lhs = 2 * (dot ** 2)
    rhs = ab_sq * bc_sq
    return lhs < rhs

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr += 1
    for _ in range(T):
        N = int(input[ptr])
        ptr