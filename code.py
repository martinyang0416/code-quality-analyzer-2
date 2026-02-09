n, m, k = map(int, input().split())
p = list(map(int, input().split()))

shift = 0
operations = 0
i = 0

while i < m:
    current_p = p[i] - shift
    current_page = (current_p - 1) // k
    upper_bound = (current_page + 1) * k + shift
    
    low = i
    high = m - 1
    best = i - 1
    while low <= high:
        mid = (low + high) // 2
        if p[mid] <= upper_bound:
            best = mid
            low = mid + 1
        else:
            high = mid - 1
    j = best + 1
    operations +=