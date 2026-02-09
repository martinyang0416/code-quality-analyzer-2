def findKthNumber(lo, hi, k):
    def get_power(x, memo={1: 0}):
        if x not in memo:
            if x % 2 == 0:
                next_x = x // 2
            else:
                next_x = 3 * x + 1
            memo[x] = 1 + get_power(next_x, memo)
        return memo[x]
    
    numbers = list(range(lo, hi + 1))
    power_list = [(get_power(num), num) for num in numbers]
    power_list.sort(key=lambda x: (x[0], x[1]))
    return power_list[k-1][1]