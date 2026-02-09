MOD = 10**9 + 7

S = input().strip()
T = input().strip()
n = len(S)

current_lt = 0
current_lt_sum = 0
current_eq = 1
current_eq_sum = 0

for i in range(n):
    s_digit = int(S[i])
    t_char = T[i]
    
    if t_char == '?':
        digits = list(range(10))
    else:
        digits = [int(t_char)]
    
    new_lt = 0
    new_lt_sum = 0
    new_eq = 0
    new_eq_sum = 0
    
    # Process transitions from eq state
    if current_eq > 0:
        for d in digits:
            if d < s_digit:
      