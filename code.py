from decimal import Decimal, getcontext

getcontext().prec = 20

T = int(input())
for _ in range(T):
    m = int(input().strip())
    percentages = input().strip().split()
    
    m_dec = Decimal(str(m))
    current = m_dec
    for p_str in percentages:
        p = Decimal(p_str)
        current *= (Decimal('1') + p / Decimal('100'))
    
    profit_percent = ((current - m_dec) / m_dec) * Decimal('100')
    
    if profit_percent >= 0:
        sign = '+'
    else:
        sign = '-'
    
    ab