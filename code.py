a1, a2, a3 = map(int, input().split())
target = a3 + 1
terms = [a1, a2]
for i in range(2, target):
    next_term = terms[-1] + terms[-2]
    terms.append(next_term)
print(terms[-1])