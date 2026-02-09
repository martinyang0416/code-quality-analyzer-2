n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

combined = A + B
unique_set = set(combined)
sorted_union = sorted(unique_set)

for num in sorted_union:
    print(num)