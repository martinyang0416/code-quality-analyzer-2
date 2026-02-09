n, m = map(int, input().split())
m_squared = m * m
if n < m_squared and n != m_squared - 1:
    print("YES")
else:
    print("NO")