def previous_permutation(arr):
    n = len(arr)
    k = n - 2
    while k >= 0 and arr[k] <= arr[k + 1]:
        k -= 1
    if k == -1:
        return arr
    l = n - 1
    while arr[l] >= arr[k]:
        l -= 1
    arr[k], arr[l] = arr[l], arr[k]
    arr[k + 1:] = arr[k + 1:][::-1]
    return arr

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    result = previous_permutation(arr)
    print(' '.join(map(str, result)))