def largestRectangleArea(heights):
    n = len(heights)
    if n == 0:
        return 0
    left = [-1] * n
    right = [n] * n
    stack = []
    
    for i in range(n):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        if stack:
            left[i] = stack[-1]
        stack.append(i)
    
    stack = []
    for i in reversed(range(n)):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        if stack:
            right[i]