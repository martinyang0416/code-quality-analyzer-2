a, b, h, w, n = map(int, input().split())
a_list = list(map(int, input().split()))

def compute_min_k(a_target, b_target, h_initial, w_initial, sorted_a):
    # Compute product needed
    if h_initial >= a_target:
        ph = 1
    else:
        ph = (a_target + h_initial - 1) // h_initial
    if w_initial >= b_target:
        pw = 1
    else:
        pw = (b_target + w_initial - 1) // w_initial
    # Compute prefix up to min(n, 40)
    max_k = min(len(sorted_a), 40)
    prefix = [1]
    for ai