a = int(input())
perm = [4, 1, 3, 2, 0, 5]
new_bits = [0] * 6

for i in range(6):
    bit = (a >> i) & 1
    new_pos = perm[i]
    new_bits[new_pos] = bit

result = 0
for j in range(6):
    result += new_bits[j] << j

print(result)