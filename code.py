dumb = input()
l = [int(o) for o in input().split()]
x, y = [int(o) for o in input().split()]

def Valid(l, k, x, y):
    s = 0
    for i in range(k):
        s += l[i]
        if s >= x and s <= y and sum(l) - s >= x and sum(l) - s <= y and s != sum(l) and s != 0 and sum(l) - s != 0:
            return True
    return False

for i in range(len(l)):
    if Valid(l, i, x, y):
        break
if i+1 > 0 and i < len(l) and Valid(l, i, x, y):
    print(i+1)
else:
    print(0)