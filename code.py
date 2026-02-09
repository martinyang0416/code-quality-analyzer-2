a1, a2, a3 = map(int, input().split())
terms = [a1, a2]
for _ in range(a3 - 1):
    next_term = terms[-1] + terms[-2]
    terms.append(next_term)
print(terms[-1])