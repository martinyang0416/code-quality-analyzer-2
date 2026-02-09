n = int(input())
sticks = [tuple(map(int, input().split())) for _ in range(n)]

prev_left = 0
prev_right = -float('inf')

for i in range(n):
    a, h = sticks[i]
    left_possible = False
    if i == 0 or (a - h > sticks[i-1][0]):
        left_possible = True
    
    right_possible = False
    if i == n-1 or (a + h < sticks[i+1][0]):
        right_possible = True
    
    max_prev = max(prev_left, prev_right)
    current_left = max_prev
    if left_possible:
        current_left = max(current_l