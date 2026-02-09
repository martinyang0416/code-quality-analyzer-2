import math

T = int(input())
for _ in range(T):
    S = input().strip()
    n = len(S)
    total = math.factorial(n)
    
    # Check presence of required characters
    kar_present = all(c in S for c in {'k', 'a', 'r'})
    shi_present = all(c in S for c in {'s', 'h', 'i'})
    
    # Calculate counts using factorial
    count_kar = math.factorial(n - 2) if kar_present else 0
    count_shi = math.factorial(n - 2) if shi_present else 0
    
    if kar_present and shi_present:
        count_both