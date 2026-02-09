from collections import defaultdict

def canArrange(arr, k):
    count = defaultdict(int)
    for num in arr:
        remainder = num % k
        count[remainder] += 1
    if count.get(0, 0) % 2 != 0:
        return False
    for i in range(1, k // 2 + 1):
        j = k - i
        if i == j:
            if count.get(i, 0) % 2 != 0:
                return False
        else:
            if count.get(i, 0) != count.get(j, 0):
                return False
    return True