def comb2(n):
    return n * (n - 1) // 2 if n >= 2 else 0

def compute(s, A, B, C):
    if s < 0:
        return 0
    a = A + 1
    b_val = B + 1
    c_val = C + 1

    c0 = comb2(s + 2)
    
    overA = comb2(s - a + 2) if s >= a else 0
    overB = comb2(s - b_val + 2) if s >= b_val else 0
    overC = comb2(s - c_val + 2) if s >= c_val else 0
    sum1 = overA + overB + overC

    overAB = comb2(s - a - b_val + 2) if s >= (a + b_val) else 0
    overAC = comb2(s - a - c_val + 2) if s >= (a + c_