tokens = input().split()
n = int(tokens[-1])
lhs_tokens = tokens[:-2]

coeff = [1]
for i in range(1, len(lhs_tokens), 2):
    op = lhs_tokens[i]
    coeff.append(1 if op == '+' else -1)

total_coeff = sum(coeff)
T = n - total_coeff

P = [i for i, c in enumerate(coeff) if c == 1]
N = [i for i, c in enumerate(coeff) if c == -1]

possible = False
if T == 0:
    possible = True
elif T > 0:
    if P and T <= len(P) * (n - 1):
        possible = True
else:
    required = -T
    if N and required <= le