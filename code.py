MOD = 10**9 + 7

def dieSimulator(n, rollMax):
    prev = [[0] * (rm + 1) for rm in rollMax]
    for j in range(6):
        if rollMax[j] >= 1:
            prev[j][1] = 1
    
    for i in range(2, n + 1):
        current = [[0] * (rm + 1) for rm in rollMax]
        for j_prev in range(6):
            max_consec_prev = rollMax[j_prev]
            for c_prev in range(1, max_consec_prev + 1):
                val = prev[j_prev][c_prev]
                if val == 0:
                    continue
     