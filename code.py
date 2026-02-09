t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b_set = set(b)
    found = False
    for num in a:
        if num in b_set:
            print("YES")
            print(f"1 {num}")
            found = True
            break
    if not found:
        print("NO")